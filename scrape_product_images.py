import requests
from bs4 import BeautifulSoup
import os
import json
from dataset import CATEGORY_ALTERNATIVES
import time
import urllib.parse
from PIL import Image
from io import BytesIO

class ImageScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }
        self.base_dir = 'product_images'
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def create_category_folder(self, category):
        """Create folder for category if it doesn't exist"""
        category_path = os.path.join(self.base_dir, category.lower().replace(' ', '_'))
        if not os.path.exists(category_path):
            os.makedirs(category_path)
        return category_path

    def is_valid_image(self, img_response):
        """Basic check for minimum image size only"""
        try:
            img = Image.open(BytesIO(img_response.content))
            width, height = img.size
            # Only filter out very small images (likely icons)
            return min(width, height) >= 100
        except:
            return False

    def download_image(self, brand, category):
        try:
            # Create category folder
            category_path = self.create_category_folder(category)
            
            # Search terms focused on product images
            search_terms = [
                f"{brand} {category} product package",
                f"{brand} {category} package",
                f"{brand} {category} product",
                f"{brand} {category}"  # fallback to simple search
            ]
            
            for search_term in search_terms:
                encoded_search = urllib.parse.quote(search_term)
                url = f"https://www.bing.com/images/search?q={encoded_search}&first=1"
                
                print(f"Searching for: {brand} using query: {search_term}")
                
                # Get the page
                response = requests.get(url, headers=self.headers)
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Try multiple images until we find a good one
                for img in soup.find_all('img', class_='mimg'):
                    src = img.get('src')
                    if src and src.startswith('http'):
                        try:
                            img_response = requests.get(src, headers=self.headers, timeout=10)
                            if img_response.status_code == 200 and self.is_valid_image(img_response):
                                
                                # Save the image
                                filename = f"{brand}.jpg".replace(' ', '_').replace('/', '_')
                                filepath = os.path.join(category_path, filename)
                                
                                with open(filepath, 'wb') as f:
                                    f.write(img_response.content)
                                
                                print(f"✓ Successfully downloaded image for {brand}")
                                return os.path.join(category.lower().replace(' ', '_'), filename)
                        except Exception as e:
                            print(f"Failed to download image: {str(e)}")
                            continue
                
                time.sleep(1)  # Small delay between different search terms
            
            print(f"✗ Failed to find image for {brand}")
            return None
            
        except Exception as e:
            print(f"Error processing {brand}: {str(e)}")
            return None

    def scrape_all(self):
        results = {}
        
        for category, brands in CATEGORY_ALTERNATIVES.items():
            print(f"\nProcessing category: {category}")
            results[category] = []
            
            for brand in brands:
                relative_path = self.download_image(brand, category)
                if relative_path:
                    results[category].append({
                        "brand": brand,
                        "image_path": relative_path,
                        "category": category
                    })
                time.sleep(2)  # Add delay between requests
        
        # Save results to JSON
        with open('product_images.json', 'w') as f:
            json.dump(results, f, indent=2)
        
        return results

def main():
    scraper = ImageScraper()
    print("Starting image scraping...")
    results = scraper.scrape_all()
    
    # Print statistics
    total = sum(len(brands) for brands in CATEGORY_ALTERNATIVES.values())
    downloaded = sum(len(os.listdir(os.path.join(scraper.base_dir, d))) 
                    for d in os.listdir(scraper.base_dir) 
                    if os.path.isdir(os.path.join(scraper.base_dir, d)))
    
    print(f"\nDownloaded {downloaded} of {total} images")
    print(f"Images saved in: {os.path.abspath(scraper.base_dir)}")

if __name__ == "__main__":
    main()