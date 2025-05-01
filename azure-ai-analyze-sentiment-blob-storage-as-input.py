Task: Example code that reads input text from a file in Azure Blob Storage public container and performs sentiment analysis
##############################################################################################################################


############
pip install azure-ai-textanalytics azure-storage-blob
###############

#### Code Here ########
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from azure.storage.blob import BlobServiceClient
import io

# Azure Language Service Configuration (hardcoded - for testing only)
LANGUAGE_ENDPOINT = "https://your-language-service.cognitiveservices.azure.com/"
LANGUAGE_KEY = "your-language-service-key"

# Azure Blob Storage Configuration (public container)
BLOB_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=yourstorageaccount;AccountKey=yourstoragekey;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "your-public-container"
BLOB_NAME = "your-text-file.txt"  # e.g., "input.txt" or "comments.txt"

def get_text_from_blob():
    """Retrieve text content from a blob in public container"""
    try:
        # Create BlobServiceClient using connection string
        blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
        
        # Get blob client
        blob_client = blob_service_client.get_blob_client(
            container=CONTAINER_NAME, 
            blob=BLOB_NAME
        )
        
        # Download blob content as text
        download_stream = blob_client.download_blob()
        return download_stream.readall().decode('utf-8')
    
    except Exception as e:
        print(f"Error accessing blob storage: {e}")
        raise

def authenticate_text_analytics_client():
    """Authenticate with Azure Language Service"""
    credential = AzureKeyCredential(LANGUAGE_KEY)
    return TextAnalyticsClient(
        endpoint=LANGUAGE_ENDPOINT,
        credential=credential
    )

def analyze_sentiment(client, text):
    """Perform sentiment analysis on the text"""
    # Split text into chunks if too large (Azure has document size limits)
    max_chunk_size = 5000  # characters
    chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]
    
    results = []
    for chunk in chunks:
        response = client.analyze_sentiment(documents=[chunk])
        for doc in response:
            results.append({
                "sentiment": doc.sentiment,
                "confidence_scores": {
                    "positive": doc.confidence_scores.positive,
                    "neutral": doc.confidence_scores.neutral,
                    "negative": doc.confidence_scores.negative
                },
                "text": chunk[:100] + "..."  # Show preview of text
            })
    return results

def main():
    try:
        # Step 1: Get text from Blob Storage
        print(f"Retrieving text from blob: {BLOB_NAME}")
        text_content = get_text_from_blob()
        print(f"Retrieved {len(text_content)} characters")
        
        # Step 2: Authenticate with Language Service
        client = authenticate_text_analytics_client()
        
        # Step 3: Analyze sentiment
        print("Analyzing sentiment...")
        results = analyze_sentiment(client, text_content)
        
        # Step 4: Display results
        print("\nSentiment Analysis Results:")
        for i, result in enumerate(results, 1):
            print(f"\nResult {i}:")
            print(f"Sentiment: {result['sentiment']}")
            print(f"Confidence - Positive: {result['confidence_scores']['positive']:.2f}")
            print(f"Confidence - Neutral: {result['confidence_scores']['neutral']:.2f}")
            print(f"Confidence - Negative: {result['confidence_scores']['negative']:.2f}")
            print(f"Text Sample: {result['text']}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
####### Code End Here #############
