import os
import requests
from pathlib import Path

def test_image_analysis(image_path):
    """Test the image analysis endpoint with a local image"""
    # API endpoint (local Flask server)
    url = "http://127.0.0.1:5000/api/upload/"
    
    # Ensure image exists
    if not os.path.exists(image_path):
        print(f"Error: Image not found at {image_path}")
        return
    
    # Prepare the image file for upload
    with open(image_path, 'rb') as image_file:
        files = {'image': ('image.jpg', image_file, 'image/jpeg')}  # Added content type
        headers = {
            'Accept': 'application/json',
        }
        
        try:
            # First, check if server is running
            health_check = requests.get("http://127.0.0.1:5000/")
            if health_check.status_code != 200:
                print("Error: Server is not running!")
                return

            # Make the POST request
            response = requests.post(url, files=files, headers=headers)
            
            # Print response for debugging
            print(f"Response Status Code: {response.status_code}")
            print(f"Response Headers: {response.headers}")
            
            # Check if request was successful
            response.raise_for_status()
            
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
                print(f"- {alt}")
                
        except requests.exceptions.ConnectionError:
            print("Error: Could not connect to server. Make sure Flask is running!")
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            if hasattr(e.response, 'text'):
                print(f"Response text: {e.response.text}")
        except Exception as e:
            print(f"Error: {e}")

def main():
    # Create a test directory if it doesn't exist
    test_dir = Path("test_images")
    test_dir.mkdir(exist_ok=True)
    
    print("Image Analysis Tester")
    print("===================")
    print("\nMake sure the Flask server is running before proceeding.")
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