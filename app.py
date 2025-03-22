import os
import io
import base64
import requests
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from google.cloud import vision
from PIL import Image
from dotenv import load_dotenv
from rapidfuzz import process
import json

# Load API key from .env file
load_dotenv("config.env")
GOOGLE_VISION_API_KEY = os.getenv("GOOGLE_VISION_API_KEY")

# Import the category data
from dataset import PRODUCT_CATEGORIES, CATEGORY_ALTERNATIVES

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def analyze_image_with_vision(image_bytes):
    """Separate function to handle Google Vision API calls"""
    vision_api_url = f"https://vision.googleapis.com/v1/images:annotate?key={GOOGLE_VISION_API_KEY}"
    
    # Encode image bytes properly for the API
    encoded_image = base64.b64encode(image_bytes).decode('utf-8')
    
    payload = {
        "requests": [{
            "image": {"content": encoded_image},
            "features": [
                {"type": "LABEL_DETECTION", "maxResults": 10},
                {"type": "LOGO_DETECTION", "maxResults": 5},
                {"type": "TEXT_DETECTION"}
            ]
        }]
    }
    
    try:
        response = requests.post(vision_api_url, json=payload)
        response.raise_for_status()
        return response.json()["responses"][0]
    except requests.exceptions.RequestException as e:
        print(f"Error calling Vision API: {e}")
        raise

@app.route("/", methods=["GET"])
def home():
    return "Server is running!"

@app.route("/api/upload/", methods=["POST", "OPTIONS"])
def analyze_image():
    # Handle preflight request
    if request.method == "OPTIONS":
        response = jsonify({"message": "preflight"})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response, 200

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    try:
        # Read the uploaded image
        image_file = request.files["image"]
        image = Image.open(image_file)

        # Convert RGBA to RGB if necessary
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        
        # Convert to JPEG format
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format="JPEG")
        img_byte_arr.seek(0)  # Reset buffer position
        img_bytes = img_byte_arr.getvalue()

        # Get Vision API results
        vision_data = analyze_image_with_vision(img_bytes)

        # Extract annotations
        labels = [label["description"].lower() for label in vision_data.get("labelAnnotations", [])]
        logos = [logo["description"].lower() for logo in vision_data.get("logoAnnotations", [])]
        
        # Extract text from image
        text_annotations = vision_data.get("textAnnotations", [])
        detected_text = text_annotations[0]["description"].lower().split() if text_annotations else []

        # Combine all detected elements
        detected_elements = labels + logos + detected_text

        # Add debug prints
        print("\nDetected Elements:")
        print("Labels:", labels)
        print("Logos:", logos)
        print("Text:", detected_text)
        print("All combined:", detected_elements)

        # Match to categories with improved scoring
        category_scores = {}
        for category, category_tags in PRODUCT_CATEGORIES.items():
            category_score = 0
            category_tags_lower = [tag.lower() for tag in category_tags]
            
            print(f"\nChecking category: {category}")
            
            for element in detected_elements:
                # Get best match from category tags
                best_match = process.extractOne(element, category_tags_lower)
                if best_match and best_match[1] > 65:  # Lowered threshold from 80 to 65
                    category_score += best_match[1]
                    print(f"Match found: '{element}' matches '{best_match[0]}' with score {best_match[1]}")
            
            if category_score > 0:
                category_scores[category] = category_score
                print(f"Total score for {category}: {category_score}")
        
        print("\nFinal Category Scores:", category_scores)

        # Find best matching category
        if category_scores:
            matched_category = max(category_scores.items(), key=lambda x: x[1])
            category_name = matched_category[0]
            alternatives = CATEGORY_ALTERNATIVES.get(category_name, ["No alternatives found"])
            
            # Get image paths for alternatives
            alternative_images = []
            for alt in alternatives:
                # Look up the image path from product_images.json
                try:
                    with open('product_images.json', 'r') as f:
                        image_data = json.load(f)
                        # Find the matching product in the category
                        for product in image_data.get(category_name, []):
                            if product['brand'] == alt:
                                # Create full URL for the image
                                image_url = f"/product_images/{product['image_path']}"
                                alternative_images.append({
                                    "brand": alt,
                                    "image_url": image_url
                                })
                                break
                except Exception as e:
                    print(f"Error loading image data: {e}")
                    alternative_images.append({
                        "brand": alt,
                        "image_url": None
                    })
            
            return jsonify({
                "detected_elements": detected_elements,
                "matched_category": category_name,
                "match_confidence": matched_category[1],
                "canadian_alternatives": alternative_images
            })
        else:
            print("\nNo categories matched with sufficient confidence")
            return jsonify({
                "error": "No matching category found",
                "detected_elements": detected_elements
            }), 404

    except Exception as e:
        print(f"Error processing request: {e}")  # Add server-side logging
        return jsonify({"error": str(e)}), 500

@app.route('/product_images/<path:filename>')
def serve_image(filename):
    return send_from_directory('product_images', filename)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)