import requests

# ---- Azure AI Computer Vision Settings ----
VISION_ENDPOINT = "https://<your-region>.api.cognitive.microsoft.com/"
VISION_SUBSCRIPTION_KEY = "your-computer-vision-subscription-key"
VISION_ANALYZE_URL = VISION_ENDPOINT + "vision/v3.2/analyze"

# ---- Public Image URL ----
IMAGE_URL = "https://storage23apr.blob.core.windows.net/storage1/cricket.jpg"

# ---- Analyze Image Using Azure Computer Vision ----
def analyze_image_from_url(image_url):
    headers = {
        'Ocp-Apim-Subscription-Key': VISION_SUBSCRIPTION_KEY,
        'Content-Type': 'application/json'
    }
    params = {
        'visualFeatures': 'Categories,Tags,Description,Objects',
        'language': 'en'
    }
    data = {
        'url': image_url
    }

    response = requests.post(
        VISION_ANALYZE_URL,
        headers=headers,
        params=params,
        json=data
    )
    response.raise_for_status()
    return response.json()

# ---- Main Execution ----
if __name__ == "__main__":
    try:
        print("Analyzing public image using Azure Computer Vision API...")
        analysis_result = analyze_image_from_url(IMAGE_URL)

        print("\n--- Analysis Result ---")
        for tag in analysis_result.get("tags", []):
            print(f"Tag: {tag['name']}, Confidence: {tag['confidence']:.2f}")

        print("\nDescription:", ", ".join(analysis_result['description']['tags']))

    except Exception as e:
        print(f"Error: {e}")
