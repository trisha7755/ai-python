import requests
from PIL import Image

import pytesseract
pytesseract.pytesseract.tesseract_cmd = "/usr/sbin/tesseract"
import io

# Function to read image from an HTTPS URL and extract text
def read_text_from_https(image_url):
    # Step 1: Download the image from the URL
    response = requests.get(image_url)
    
    if response.status_code == 200:
        # Step 2: Load the image using Pillow
        img = Image.open(io.BytesIO(response.content))
        
        # Step 3: Use pytesseract to extract text from the image
        text = pytesseract.image_to_string(img)
        
        # Step 4: Return the extracted text
        return text
    else:
        return f"Failed to retrieve image. Status code: {response.status_code}"

# Example usage
image_url = 'https://aemdemoclass1.blob.core.windows.net/aimlsnap/schedule1.jpeg'  # Replace with the actual URL of the image

extracted_text = read_text_from_https(image_url)
print("Extracted Text:")
print(extracted_text)

