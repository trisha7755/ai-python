# Install transformers and other required libraries
!pip install transformers pillow requests

# Import necessary libraries
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import requests
import torch

def generate_caption(image_url):
    # Load the image from the URL
    image = Image.open(requests.get(image_url, stream=True).raw)
    
    # Load the pre-trained image captioning model and tokenizer
    model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

    # Preprocess the image
    pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values

    # Generate caption
    generated_ids = model.generate(pixel_values, max_length=16, num_beams=4, early_stopping=True)
    caption = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    
    return caption

# Example usage: Replace the image URL below with your desired image URL
image_url = "https://example.com/sample-image.jpg"
caption = generate_caption(image_url)
print(f"Generated Caption: {caption}")
