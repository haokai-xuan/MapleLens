import os
import requests
from pathlib import Path

def test_image_analysis(image_path):
    """Test the image analysis endpoint with a local image"""
    # API endpoint (Vercel deployment)
    base_url = "https://maple-lens-three.vercel.app"  # Update this to your final Vercel URL
    url = f"{base_url}/api/upload/"
    
    # Ensure image exists
    if not os.path.exists(image_path):
        print(f"Error: Image not found at {image_path}")
        return
    
    # Prepare the image file for upload
    with open(image_path, 'rb') as image_file:
        files = {'image': ('image.jpg', image_file, 'image/jpeg')}
        headers = {
            'Accept': 'application/json',
            'Origin': 'https://maple-lens-three.vercel.app'
        }
        
        try:
            # Make the POST request directly without health check
            print(f"Sending request to {url}...")
            response = requests.post(
                url, 
                files=files, 
                headers=headers,
                timeout=30  # Add timeout
            )
            
            # Print response for debugging
            print(f"\nResponse Status Code: {response.status_code}")
            print(f"Response Headers: {response.headers}")
            
            if response.status_code == 200:
                # Print results
                result = response.json()
                print("\nAnalysis Results:")
                print("================")
                print(f"Detected Elements: {result.get('detected_elements', [])}")
                print(f"Matched Category: {result.get('matched_category', 'None')}")
                print(f"Match Confidence: {result.get('match_confidence', 0)}")
                print("\nCanadian Alternatives:")
                print("=====================")
                for alt in result.get('canadian_alternatives', []):
                    print(f"Brand: {alt.get('brand')}")
                    print(f"Image URL: {alt.get('image_url')}")
                    print("---")
            else:
                print(f"\nError Response: {response.text}")
                
        except requests.exceptions.ConnectionError:
            print(f"Error: Could not connect to {url}")
            print("Please check if the URL is correct and the server is deployed properly.")
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response text: {e.response.text}")
        except Exception as e:
            print(f"Error: {e}")

def main():
    # Create a test directory if it doesn't exist
    test_dir = Path("test_images")
    test_dir.mkdir(exist_ok=True)
    
    print("MapleLens API Tester")
    print("===================")
    print("\nThis tool will test the deployed Vercel API endpoint.")
    print("Place your test images in the 'test_images' directory.")
    
    # List available images
    images = list(test_dir.glob("*.*"))
    
    if not images:
        print("\nNo images found in test_images directory!")
        print("Please add some images and try again.")
        return
    
    print("\nAvailable test images:")
    for i, image_path in enumerate(images, 1):
        print(f"{i}. {image_path.name}")
    
    # Let user select an image
    while True:
        try:
            choice = int(input("\nEnter the number of the image to test (0 to exit): "))
            if choice == 0:
                break
            if 1 <= choice <= len(images):
                print(f"\nTesting image: {images[choice-1]}")
                test_image_analysis(str(images[choice-1]))
            else:
                print("Invalid choice!")
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()