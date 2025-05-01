import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def authenticate_client():
    # Replace these with your actual Azure Language Service credentials
    language_endpoint = "https://your-resource-name.cognitiveservices.azure.com/"
    language_key = "your-32-character-azure-key-here"
    
    ta_credential = AzureKeyCredential(language_key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=language_endpoint, 
        credential=ta_credential)
    return text_analytics_client

def sentiment_analysis_example(client):
    documents = [
        "I had the best day of my life. I wish you were there with me.",
        "This was a waste of my time. The speaker put me to sleep.",
        "No complaints."
    ]
    
    response = client.analyze_sentiment(documents=documents)
    for doc in response:
        print(f"Document: {documents[response.index(doc)]}")
        print(f"Overall sentiment: {doc.sentiment}")
        print(f"Scores: positive={doc.confidence_scores.positive:.2f}, neutral={doc.confidence_scores.neutral:.2f}, negative={doc.confidence_scores.negative:.2f}")
        print()

if __name__ == "__main__":
    try:
        client = authenticate_client()
        sentiment_analysis_example(client)
    except Exception as err:
        print(f"Error occurred: {err}")
