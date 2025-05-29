# This program will translate English to french with Azure AI Foundry Translate Playground key and Endpoint with specific region
import os
import requests
import json

class AzureTranslator:
    def __init__(self, endpoint, key, location):
        self.endpoint = endpoint
        self.key = key
        self.location = location
        self.url = f"{self.endpoint}/translator/text/v3.0/translate"
    
    def translate(self, text, from_lang='en', to_lang='fr'):
        headers = {
            'Ocp-Apim-Subscription-Key': self.key,
            'Ocp-Apim-Subscription-Region': self.location,
            'Content-Type': 'application/json'
        }
        
        params = {
            'api-version': '3.0',
            'from': from_lang,
            'to': to_lang
        }
        
        body = [{'text': text}]
        
        try:
            response = requests.post(self.url, headers=headers, params=params, json=body)
            response.raise_for_status()
            
            translation = response.json()
            return translation[0]['translations'][0]['text']
        except Exception as e:
            print(f"Error during translation: {e}")
            return None

def main():
    # Azure Translator configuration
    endpoint = "https://project13318301334.cognitiveservices.azure.com/"
    key = "AxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxGwibK"
    location = "westus"
    
    # Create translator instance
    translator = AzureTranslator(endpoint, key, location)
    
    print("English to French Translator (using Azure AI)")
    print("Type 'quit' to exit\n")
    
    while True:
        text = input("Enter English text to translate: ")
        
        if text.lower() == 'quit':
            break
            
        if text.strip():
            translation = translator.translate(text)
            if translation:
                print(f"French translation: {translation}\n")
            else:
                print("Translation failed. Please try again.\n")
        else:
            print("Please enter some text to translate.\n")

if __name__ == "__main__":
    main()
