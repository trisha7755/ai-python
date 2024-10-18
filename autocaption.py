%sh
pip install transformers torch pillow requests

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

def generate_caption(image_url):
    # Load the image from the URL
    image = Image.open(requests.get(image_url, stream=True).raw)
    
    # Load the pre-trained BLIP model and processor
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    
    # Preprocess the image and prepare input for the model
    inputs = processor(image, return_tensors="pt")
    
    # Generate caption
    caption_ids = model.generate(**inputs)
    caption = processor.decode(caption_ids[0], skip_special_tokens=True)
    
    return caption

# Example usage
image_url = "https://example.com/sample-image.jpg"
caption = generate_caption(image_url)
print(f"Generated Caption: {caption}")
