import os
from pypdf import PdfReader
import re
from pathlib import Path

def get_pdf_title(pdf_path):
    """Get PDF title from metadata, fallback to content extraction if needed."""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            
            # Try to get title from metadata first
            metadata_title = pdf_reader.metadata.get('/Title', '')
            
            if metadata_title and len(metadata_title.strip()) >= 10:
                return clean_title(metadata_title)
            
            # If no metadata title, extract from first page content
            first_page = pdf_reader.pages[0]
            text = first_page.extract_text()
            
            # Get first non-empty line that's at least 10 characters long
            lines = [line.strip() for line in text.split('\n')]
            title = next((line for line in lines if len(line) >= 10), "Untitled")
            
            return clean_title(title)
            
    except Exception as e:
        print(f"Error processing {pdf_path}: {str(e)}")
        return "Untitled"

def clean_title(title):
    """Clean and format the title for use as filename."""
    # Remove special characters and replace with spaces
    title = re.sub(r'[^\w\s-]', ' ', title)
    
    # Replace multiple spaces with single space
    title = re.sub(r'\s+', ' ', title)
    
    # Trim to reasonable length (max 50 characters)
    title = title[:50].strip()
    
    # Remove any leading/trailing spaces or dots
    title = title.strip('. ')
    
    # Replace spaces with underscores
    title = title.replace(' ', '_')
    
    return title

def rename_pdfs_in_folder(folder_path):
    """Rename all PDFs in the specified folder based on their titles."""
    folder = Path(folder_path)
    pdf_files = list(folder.glob('*.pdf'))
    
    print(f"Found {len(pdf_files)} PDF files")
    
    for pdf_file in pdf_files:
        try:
            # Get title from PDF
            new_title = get_pdf_title(pdf_file)
            
            # Create new filename
            new_filename = f"{new_title}.pdf"
            new_path = pdf_file.parent / new_filename
            
            # Ensure filename is unique
            counter = 1
            while new_path.exists():
                new_filename = f"{new_title}_{counter}.pdf"
                new_path = pdf_file.parent / new_filename
                counter += 1
            
            # Rename the file
            pdf_file.rename(new_path)
            print(f"Renamed: {pdf_file.name} -> {new_filename}")
            
        except Exception as e:
            print(f"Error renaming {pdf_file.name}: {str(e)}")

if __name__ == "__main__":
    # First install required package:
    # pip install pypdf
    
    folder_path = "downloaded_presentations"  # Change this to your folder path
    rename_pdfs_in_folder(folder_path)
