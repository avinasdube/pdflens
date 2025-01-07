import customtkinter as ctk
from PIL import Image
from src.pdf_processing import open_pdf
from src.utils import save_text, clear_text, search_and_highlight

# initializing appearance and theme
ctk.set_appearance_mode("Light")  # Light/Dark mode
ctk.set_default_color_theme("./assets/theme.json")  # Custom theme

# loading necessary images
openfileimg = Image.open("./assets/icons/openfile.png")
savefileimg = Image.open("./assets/icons/savetext.png")
cleartextimg = Image.open("./assets/icons/cleartext.png")
searchicon = Image.open("./assets/icons/searchicon.png")

# main application class
class PDFtoTextApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PDF Lens")
        self.geometry("800x500")
        self.minsize(width=300, height=420)
        self.iconbitmap("./assets/icons/pdflens.ico")
        
        # configuring grid layout
        self.grid_rowconfigure(0, weight=0)  # Banner row
        self.grid_rowconfigure(1, weight=0)  # File button row
        self.grid_rowconfigure(2, weight=0)  # Search button row
        self.grid_rowconfigure(3, weight=1)  # Text box row (expands)
        self.grid_rowconfigure(4, weight=0)  # Buttons frame row
        self.grid_rowconfigure(5, weight=0)  # Footer row
        self.grid_columnconfigure(0, weight=1)  # Single column layout
        
        # adding banner at the top
        self.banner = ctk.CTkLabel(
            self, 
            text="Welcome to PDF Lens! Convert your PDF to Text seamlessly.", 
            font=ctk.CTkFont(family="Helvetica",size=28, weight="bold"), 
            fg_color="transparent",  # Banner background
            text_color="black", # Text color
            anchor="w",
            corner_radius=10
        )
        self.banner.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        
        # dynamically wrapping banner according to current window width
        self.bind("<Configure>", lambda event: self.adjust_banner_wraplength())

        # defining open PDF button
        self.file_button = ctk.CTkButton(
            self, 
            text="Open PDF", 
            corner_radius=10, 
            image=ctk.CTkImage(dark_image=openfileimg, light_image=openfileimg), 
            command=self.open_pdf_action
        )
        self.file_button.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        
        # setting frame for search bar and button
        self.search_frame = ctk.CTkFrame(self)
        self.search_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.search_frame.grid_columnconfigure(0, weight=1)  # Search bar column (expandable)
        self.search_frame.grid_columnconfigure(1, weight=0)  # Search button column (fixed)

        # defining search box field
        self.search_bar = ctk.CTkEntry(
            self.search_frame,
            corner_radius=10,
            fg_color="white",
            border_width=0,
            placeholder_text="Search your keywords here ...",
            font=ctk.CTkFont(family="Helvetica", weight='normal'),
        )
        self.search_bar.grid(row=0, column=0, padx=(0, 10), sticky="ew")  # Add some spacing to the right

        # defining search button
        self.search_button = ctk.CTkButton(
            self.search_frame,
            text=None,
            image=ctk.CTkImage(dark_image=searchicon, light_image=searchicon),
            command=self.search_text_action,
            bg_color="transparent",
            fg_color=self.search_frame.cget("fg_color"),  # Match parent frame's color
            hover_color=self.search_frame.cget("fg_color"),  # Same as parent frame
            width=30,  # Adjust size as needed
            height=30,  # Adjust size as needed
        )
        self.search_button.grid(row=0, column=1, sticky="e")  # Align to the end of the row

        # defining text box for displaying PDF content
        self.text_box = ctk.CTkTextbox(self, width=750, height=400, corner_radius=20)
        self.text_box.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")

        # setting frame for action buttons
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.grid(row=4, column=0, pady=10, sticky="ew")
        self.button_frame.grid_columnconfigure(0, weight=1)  # Left spacing
        self.button_frame.grid_columnconfigure(1, weight=0)  # Save button
        self.button_frame.grid_columnconfigure(2, weight=1)  # Right spacing

        # defining save and clear buttons
        self.save_button = ctk.CTkButton(
            self.button_frame, 
            text="Save Text", 
            corner_radius=10, 
            image=ctk.CTkImage(dark_image=savefileimg, light_image=savefileimg), 
            command=self.save_text_action
        )
        
        self.clear_button = ctk.CTkButton(
            self.button_frame, 
            text="Clear", 
            corner_radius=10, 
            image=ctk.CTkImage(dark_image=cleartextimg, light_image=cleartextimg), 
            command=self.clear_text_action
        )
        
        # setting action buttons alignment
        self.save_button.grid(row=0, column=0, padx=20)
        self.clear_button.grid(row=0, column=2, padx=20)
        
        # adding banner at the top
        self.footer = ctk.CTkLabel(
            self, 
            text="Developed By - Avinash Dubey, Copyright 2025", 
            font=ctk.CTkFont(family="Helvetica",size=12, weight="normal"), 
            fg_color="transparent",  # Banner background
            text_color="gray", # Text color
            anchor="center",
        )
        self.footer.grid(row=5, column=0, sticky="nsew", padx=20, pady=20)
    
    # function to update banner wraplength dynamically based on window width
    def adjust_banner_wraplength(self):
        window_width = self.winfo_width()
        self.banner.configure(wraplength=window_width - 40)  # 40px for padding

    # defining action methods
    def open_pdf_action(self):
        open_pdf(self.text_box)
    
    def search_text_action(self):
        search_query = self.search_bar.get() # getting text from search bar
        search_and_highlight(self.text_box, search_query)

    def save_text_action(self):
        save_text(self.text_box)

    def clear_text_action(self):
        clear_text(self.text_box)
