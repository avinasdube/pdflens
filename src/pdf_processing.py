# This file includes functions related to PDF processing.

from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader

# defining function to open pdf in the text box
def open_pdf(text_box):
    """Opens a PDF file and displays its text in the provided text box."""
    
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    
    if not file_path:
        return

    try:
        reader = PdfReader(file_path)
        extracted_text = ""
        for page in reader.pages:
            text = page.extract_text()
            extracted_text += text + "\n" if text else "[Could not extract text from this page]\n"
        
        text_box.delete("1.0", "end")  # clear existing text
        text_box.insert("1.0", extracted_text)  # insert the extracted text
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open PDF: {str(e)}")

    