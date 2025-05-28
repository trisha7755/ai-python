import requests
import json

class AzureAITranslator:
    def __init__(self, endpoint, subscription_key, region=None):
        """
        Initialize the translator with Azure AI Translator endpoint and subscription key
        
        Args:
            endpoint (str): Azure AI Translator endpoint URL
                          (e.g., "https://api.cognitive.microsofttranslator.com")
            subscription_key (str): Subscription key for authentication
            region (str): [Optional] Your Azure resource region (e.g., "eastus")
        """
        # Clean up endpoint (remove trailing slash if present)
        self.endpoint = endpoint.rstrip('/')
        self.subscription_key = subscription_key
        self.region = region
        
        self.headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key,
            'Content-Type': 'application/json',
        }
        
        # Add region to headers if provided (required for some endpoints)
        if self.region:
            self.headers['Ocp-Apim-Subscription-Region'] = self.region
        
    def translate(self, text, from_lang='en', to_lang='bn'):
        """
        Translate text from source language to target language
        
        Args:
            text (str): Text to translate
            from_lang (str): Source language code (default: 'en' for English)
            to_lang (str): Target language code (default: 'bn' for Bengali)
            
        Returns:
            str: Translated text or None if failed
        """
        # Construct the request body
        body = [{
            'text': text
        }]
        
        # Construct the URL with query parameters
        params = {
            'api-version': '3.0',
            'from': from_lang,
            'to': to_lang
        }
        
        try:
            # Make the POST request to the translation endpoint
            response = requests.post(
                f"{self.endpoint}/translate",
                headers=self.headers,
                params=params,
                json=body
            )
            
            response.raise_for_status()  # Raise exception for bad status codes
            
            # Parse the response
            translation = response.json()
            translated_text = translation[0]['translations'][0]['text']
            
            return translated_text
            
        except requests.exceptions.RequestException as e:
            print(f"Error during translation request: {str(e)}")
            if hasattr(e, 'response') and e.response:
                print(f"Status code: {e.response.status_code}")
                print(f"Response: {e.response.text}")
            return None
        except (KeyError, IndexError) as e:
            print(f"Error parsing translation response: {str(e)}")
            return None


# Example usage with corrected endpoint
if __name__ == "__main__":
    # Get these values from your Azure portal:
    # 1. Go to your Translator resource
    # 2. Look under "Keys and Endpoint"
    ENDPOINT = "https://api.cognitive.microsofttranslator.com"  # Default global endpoint
    # OR use your custom endpoint if you have one:
    # ENDPOINT = "https://<your-resource-name>.cognitiveservices.azure.com/translator/text/v3.0"
    
    SUBSCRIPTION_KEY = "your-actual-subscription-key"  # Replace with your key
    REGION = "eastus"  # Your resource region, e.g., "eastus", "westeurope", etc.
    
    # Initialize the translator
    translator = AzureAITranslator(ENDPOINT, SUBSCRIPTION_KEY, REGION)
    
    # Text to translate
    english_text = "Hello, how are you today?"
    
    # Translate to Bengali
    bengali_text = translator.translate(english_text)
    
    if bengali_text:
        print(f"English: {english_text}")
        print(f"Bengali: {bengali_text}")
    else:
        print("Translation failed.")
