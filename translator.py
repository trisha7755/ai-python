import requests
import json

class AzureAITranslator:
    def __init__(self, endpoint, subscription_key):
        """
        Initialize the translator with Azure AI Foundry endpoint and subscription key
        
        Args:
            endpoint (str): Azure AI Foundry endpoint URL
            subscription_key (str): Subscription key for authentication
        """
        self.endpoint = endpoint
        self.subscription_key = subscription_key
        self.headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key,
            'Content-Type': 'application/json',
        }
        
    def translate(self, text, from_lang='en', to_lang='bn'):
        """
        Translate text from source language to target language
        
        Args:
            text (str): Text to translate
            from_lang (str): Source language code (default: 'en' for English)
            to_lang (str): Target language code (default: 'bn' for Bengali)
            
        Returns:
            str: Translated text
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
            print(f"Error during translation request: {e}")
            return None
        except (KeyError, IndexError) as e:
            print(f"Error parsing translation response: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Replace these with your actual Azure AI Foundry values
    ENDPOINT = "https://api.example.cognitive.microsofttranslator.com"  # Your endpoint
    SUBSCRIPTION_KEY = "your-subscription-key"  # Your subscription key
    
    # Initialize the translator
    translator = AzureAITranslator(ENDPOINT, SUBSCRIPTION_KEY)
    
    # Text to translate
    english_text = "Hello, how are you today?"
    
    # Translate to Bengali
    bengali_text = translator.translate(english_text)
    
    if bengali_text:
        print(f"English: {english_text}")
        print(f"Bengali: {bengali_text}")
    else:
        print("Translation failed.")
