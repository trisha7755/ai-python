from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from openai import AzureOpenAI
import os

# --- Azure AI Foundry Config ---
DOCUMENT_INTELLIGENCE_ENDPOINT = "https://hub12998583260.cognitiveservices.azure.com/"
DOCUMENT_INTELLIGENCE_KEY = "8miuOJID9KKLdeM8Tw5KkXoKdJwd9HBGglCxaTUtZ8opEvjOEh97JQQJ99BEACYeBjFXJ3w3AAAAACOGc6U7"

def summarize_with_ai_language(text):
    """Fallback: Use Azure AI Language's summarization (preview)."""
    from azure.ai.textanalytics import TextAnalyticsClient
    
    client = TextAnalyticsClient(
        endpoint=DOCUMENT_INTELLIGENCE_ENDPOINT,  # Same endpoint (if enabled)
        credential=AzureKeyCredential(DOCUMENT_INTELLIGENCE_KEY)
    
    poller = client.begin_abstract_summary([text])
    result = poller.result()
    return result[0].summaries[0].text

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    pdf_path = "your_document.pdf"  # Replace with your PDF
    
    # Step 1: Extract text
    print("Extracting text from PDF...")
    extracted_text = extract_text_from_pdf(pdf_path)
    print(f"Extracted {len(extracted_text)} characters.")
    
    # Step 2: Summarize (prefer OpenAI if available)
    print("\nSummarizing...")
    if AZURE_OPENAI_KEY != "YOUR_AZURE_OPENAI_KEY":
        summary = summarize_with_openai(extracted_text)
    else:
        summary = summarize_with_ai_language(extracted_text)
    
    print("\n--- SUMMARY ---")
    print(summary)
