# This file includes functions related to text utility

import tkinter as tk
from tkinter import filedialog, messagebox

# function to save selected text to a specified file
def save_text(text_box):
    
    # get the selected text, if any
    try:
        selected_text = text_box.get("sel.first", "sel.last")
    except tk.TclError:
        selected_text = ""  # no text selected

    # if selected text exists, use it; otherwise, use the full text
    text_to_save = selected_text if selected_text else text_box.get("1.0", "end").strip()

    if not text_to_save:
        messagebox.showwarning("Warning", "Text box is empty!")
        return

    # ask user where to save the file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return  # if no file path is chosen, return without saving
    
    # try saving the text to the selected file
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_to_save)
        messagebox.showinfo("Success", "Text saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save text: {str(e)}")


def clear_text(text_box):
    text_box.delete("1.0", "end")