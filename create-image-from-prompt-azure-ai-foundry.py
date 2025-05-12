import os
from openai import AzureOpenAI

# You will need to set these environment variables or edit the following values.
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "https://hub1234886090677.openai.azure.com/")
api_version = os.getenv("OPENAI_API_VERSION", "2024-04-01-preview")
deployment = os.getenv("DEPLOYMENT_NAME", "dall-e-3")
api_key = os.getenv("AZURE_OPENAI_API_KEY", "4pWxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx2")

# Initialize the client
client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=api_key,
)

def generate_image():
    # Get prompt from user
    prompt = input("Please enter your image description: ")
   
    if not prompt:
        print("No prompt provided. Using default prompt.")
        prompt = "a beautiful sunrise over mountains"
   
    print(f"Generating image for: {prompt}...")
   
    try:
        # Generate the image
        result = client.images.generate(
            model=deployment,
            prompt=prompt,
            n=1,
            style="vivid",
            quality="standard",
        )
       
        # Get the image URL
        image_url = result.data[0].url
        print("\nImage generated successfully!")
        print(f"Image URL: {image_url}")
        print("\nYou can download the image by:")
        print(f"1. Right-clicking the URL and selecting 'Save link as...'")
        print(f"2. Or opening the URL in your browser and saving the image")
       
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate_image()
