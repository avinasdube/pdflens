import customtkinter as ctk

# importing functions for PDF handling and text manipulation
from src.pdf_processing import open_pdf
from src.utils import save_text, clear_text

# setting up the appearance of the application
ctk.set_appearance_mode("System")  # following system's light/dark mode
ctk.set_default_color_theme("./assets/theme.json")  # loading custom color theme

# defining the main application class that inherits from ctk.CTk
class PDFtoTextApp(ctk.CTk):
    # initializing constructor and creating necessary widgets
    def __init__(self):
        
        # initializing the base class and setting up the window properties
        super().__init__()
        self.title("PDF Lens")  # title of the window
        self.geometry("800x600")  # window size

        # creating and configuring the "Open PDF" button
        self.file_button = ctk.CTkButton(self, text="Open PDF", corner_radius=10, command=self.open_pdf_action)
        self.file_button.pack(pady=10)  # packing the button with padding

        # creating a multi-line text box for displaying PDF content
        self.text_box = ctk.CTkTextbox(self, width=750, height=400, corner_radius=20)
        self.text_box.pack(pady=10)  # packing the text box with padding

        # Creating the "Save Text" button
        self.save_button = ctk.CTkButton(self, text="Save Text", corner_radius=10, command=self.save_text_action)
        self.save_button.pack(side="left", padx=20, pady=10)  # packing the button on the left side with padding

        # creating the "Clear" button
        self.clear_button = ctk.CTkButton(self, text="Clear", corner_radius=10, command=self.clear_text_action)
        self.clear_button.pack(side="right", padx=20, pady=10)  # packing the button on the right side with padding
    
    # action method to open and extract text from a PDF
    def open_pdf_action(self):
        # calling the open_pdf function from pdf_processing module
        open_pdf(self.text_box)

    # action method to save the extracted text
    def save_text_action(self):
        # calling the save_text function from utils module
        save_text(self.text_box)

    # Action method to clear the text box
    def clear_text_action(self):
        # calling the clear_text function from utils module
        clear_text(self.text_box)

