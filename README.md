# PDF Lens - A PDF Text Converter and Search Tool

Welcome to the **PDF Lens**! This Python-based application allows you to extract text from PDF files, search for specific keywords, and highlight them for easier identification. It also includes a user-friendly graphical interface for seamless interaction.

---

## **Features**

1. **Extract Text**:
   - Extract text from any PDF file quickly and efficiently.
2. **Search Keywords**:
   - Search for single or multiple keywords within the extracted text.
   - Highlight keywords for better visibility.
3. **Save Results**:
   - Option to save the extracted or processed text for future use.
4. **Graphical Interface**:
   - Simple and intuitive interface built with Tkinter.
5. **Error Handling**:
   - Gracefully handles missing files, invalid inputs, and large documents.

---

## **Technologies Used**

- **Python**: Core programming language for the project.
- **PyPDF2**: For extracting text from PDF files.
- **re (Regular Expressions)**: For keyword searching and highlighting.
- **Tkinter**: For creating a beautiful and user-friendly GUI.

---

## **Installation Guide**

### **Prerequisites**

1. **Python**:
   - Download and install Python 3.7 or higher from [python.org](https://www.python.org/).
   - Ensure Python is added to your system PATH.

2. **Install Required Libraries**:
   Run the following command to install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **Clone the Repository**

```bash
git clone https://github.com/avinasdube/pdflens.git
cd pdflens
```

---

## **How to Run**

1. Navigate to the project directory:
   ```bash
   cd pdflens
   ```

2. Run the application:
   ```bash
   python main.py
   ```

---

## **Usage Instructions**

1. Open the application.
2. Use the "Browse" button to select a PDF file.
3. Enter the keyword(s) to search.
4. Click "Search" to view the highlighted results in the text area.
5. Optionally, save the processed text to a file for later use.

---

## **Folder Structure**

```
pdflens/
|
├── assets/               # Icons and additional resources
├── src/                  # Source code
│   ├── __init__.py       # Package initializer
│   ├── gui.py            # GUI logic
│   ├── pdf_processing.py # Core logic for PDF text extraction
│   ├── utils.py          # Helper functions
|
├── tests/                # Unit tests
│   ├── test_pdf_processing.py
│   ├── test_gui.py
|
├── requirements.txt      # Dependencies
├── setup.py              # Packaging script
├── README.md             # Documentation
└── main.py               # Entry point
```

---

## **Advanced Features**

- **Multi-Keyword Search**:
  - Enter multiple keywords separated by commas for advanced search capabilities.
- **Save Results to File**:
  - Save the processed or highlighted text as a `.txt` or `.pdf` file.
- **Performance Optimization**:
  - Optimized for handling large PDFs by processing pages incrementally.

---

## **Future Enhancements**

1. **PDF Viewer**:
   - Embed a PDF viewer to display the original document alongside the extracted text.
2. **Text-to-Speech Integration**:
   - Add an option to convert the extracted text to speech.
3. **Cloud Integration**:
   - Save and retrieve PDFs and results from cloud storage.

---

## **Author**

**Avinash Dubey**

If you have any suggestions, feedback, or issues, feel free to contact me at **avidubey712@gmail.com**.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Acknowledgements**

Special thanks to the contributors and libraries that made this project possible:

- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [ReportLab](https://www.reportlab.com/)

---

Thank you for using the **PDF Lens**! 🚀

