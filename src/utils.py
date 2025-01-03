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

# function to clear text inside text box
def clear_text(text_box):
    text_box.delete("1.0", "end")

# function to search a word and highlight it
def search_and_highlight(text_box, search_query, tag_name="highlight", highlight_bg="yellow", highlight_fg="black"):
    """
    Searches for the specified query in a text widget and highlights all matches.
    
    Parameters:
        text_widget: The text widget to search in (e.g., a CTkTextbox).
        search_query: The query to search for.
        tag_name: The tag name to apply for highlights.
        highlight_bg: Background color for the highlight.
        highlight_fg: Foreground (text) color for the highlight.
    """
    # clear previous highlights
    text_box.tag_remove(tag_name, "1.0", "end")
    
    if search_query:
        start_pos = "1.0"
        while True:
            # find the start and end indices of the match
            start_pos = text_box.search(search_query, start_pos, stopindex="end", nocase=True)
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(search_query)}c"
            
            # highlight the match
            text_box.tag_add(tag_name, start_pos, end_pos)
            start_pos = end_pos  # Move to the next position
            
        # configure the highlight tag
        text_box.tag_config(tag_name, background=highlight_bg, foreground=highlight_fg)
