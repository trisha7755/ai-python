import requests
import json
import os
import PyPDF2

def download_pdf(url, save_path):
    """Download a PDF from a URL and save it locally."""
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"PDF downloaded successfully: {save_path}")
        return True
    else:
        print(f"Failed to download PDF. Status Code: {response.status_code}")
        return False

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error extracting text: {e}")
    return text.strip()

def save_json(data, json_path):
    """Save extracted text into a JSON file."""
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({"content": data}, f, indent=4)
    print(f"JSON saved successfully: {json_path}")

def main():
    pdf_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"  # Replace with your PDF URL
    pdf_path = "downloaded_file.pdf"
    json_path = "output.json"

    if download_pdf(pdf_url, pdf_path):
        extracted_text = extract_text_from_pdf(pdf_path)
        if extracted_text:
            save_json(extracted_text, json_path)
        else:
            print("No text extracted from the PDF.")
    else:
        print("Failed to process PDF.")

if __name__ == "__main__":
    main()
