import fitz  # PyMuPDF
from transformers import pipeline

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text("text") + "\n"
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def summarize_text(text, max_length=300):
    """Summarize text using a pre-trained model."""
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarizer(text, max_length=max_length, min_length=100, do_sample=False)[0]["summary_text"]

def main():
    pdf_path = input("Enter the PDF file name (with extension): ").strip()
    
    text = extract_text_from_pdf(pdf_path)
    if not text:
        print("Failed to extract text. Please check the file path and try again.")
        return
    
    if len(text) < 100:
        print("Text is too short for summarization.")
        return
    
    summary = summarize_text(text)
    print("\n--- Summary ---\n", summary)

if __name__ == "__main__":
    main()
