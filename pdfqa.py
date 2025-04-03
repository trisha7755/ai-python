import re
import PyPDF2
from typing import List, Dict

class PDFAnswerExtractor:
    def __init__(self, pdf_path: str):
        """
        Initialize the PDFAnswerExtractor with the path to the PDF file.
        
        Args:
            pdf_path (str): Path to the PDF file to extract answers from.
        """
        self.pdf_path = pdf_path
        self.text = self._extract_text_from_pdf()
    
    def _extract_text_from_pdf(self) -> str:
        """
        Extract all text from the PDF file.
        
        Returns:
            str: Concatenated text from all pages of the PDF.
        """
        text = ""
        with open(self.pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
    
    def find_answer(self, question: str) -> str:
        """
        Find answer to a specific question in the PDF text.
        
        Args:
            question (str): Question to search answer for.
            
        Returns:
            str: The found answer or a message indicating answer wasn't found.
        """
        # Find the question in the text
        question_pattern = re.escape(question)
        match = re.search(question_pattern, self.text, re.IGNORECASE)
        
        if match:
            # Extract text after the question (potential answer)
            start_pos = match.end()
            end_pos = start_pos + 500  # Look at next 500 characters
            potential_answer = self.text[start_pos:end_pos].strip()
            
            # Clean up the answer (remove extra whitespace, newlines)
            potential_answer = ' '.join(potential_answer.split())
            
            # Try to find the end of the answer (look for next question or section)
            end_markers = ["\n\n", "Question", "Q:", "Problem", "Next"]
            end_position = len(potential_answer)
            
            for marker in end_markers:
                marker_pos = potential_answer.find(marker)
                if 0 < marker_pos < end_position:
                    end_position = marker_pos
            
            final_answer = potential_answer[:end_position].strip()
            return final_answer if final_answer else "Answer found but empty"
        else:
            return "Answer not found in the document"
    
    def interactive_mode(self):
        """
        Start an interactive session where user can ask questions one by one.
        """
        print("\n" + "="*50)
        print("PDF Answer Extractor - Interactive Mode")
        print("="*50)
        print(f"\nLoaded PDF: {self.pdf_path}")
        print("Type your questions one at a time. Enter 'quit' to exit.\n")
        
        while True:
            question = input("\nWhat question would you like to search for? (or 'quit' to exit): ").strip()
            
            if question.lower() in ['quit', 'exit', 'q']:
                print("\nExiting interactive mode. Goodbye!")
                break
            
            if not question:
                print("Please enter a question.")
                continue
            
            print("\nSearching for answer...")
            answer = self.find_answer(question)
            
            print("\n" + "-"*50)
            print(f"Question: {question}")
            print(f"Answer: {answer}")
            print("-"*50)

# Example usage
if __name__ == "__main__":
    # Get PDF file path from user
    pdf_path = input("Enter the path to your PDF file: ").strip()
    
    try:
        # Initialize the extractor
        extractor = PDFAnswerExtractor(pdf_path)
        
        # Start interactive mode
        extractor.interactive_mode()
    
    except FileNotFoundError:
        print(f"\nError: The file '{pdf_path}' was not found. Please check the path and try again.")
    except PyPDF2.PdfReaderError:
        print(f"\nError: The file '{pdf_path}' is not a valid PDF or is corrupted.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
