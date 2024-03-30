import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Function to create directories if they don't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to organize files into respective folders
def organize_files(source_dir):
    # Define file extensions and their corresponding folders
    file_extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'Compressed': ['.zip', '.rar', '.7z'],
        'Software': ['.exe', '.msi'],
        'Documents': ['.docx', '.pdf', '.pptx', '.txt','.xlsx']
    }

    # Iterate through each file in the source directory
    for filename in os.listdir(source_dir):
        filepath = os.path.join(source_dir, filename)

        # Skip directories
        if os.path.isdir(filepath):
            continue

        # Determine the file extension
        _, ext = os.path.splitext(filename)

        # Move the file to the corresponding directory
        for category, extensions in file_extensions.items():
            if ext.lower() in extensions:
                dest_dir = os.path.join(source_dir, category)
                create_directory(dest_dir)
                shutil.move(filepath, dest_dir)
                print(f"Moved {filename} to {category} folder")
                break

# Function to copy selected file
def copy_file():
    selected_file = file_listbox.get(tk.ACTIVE)
    source_dir = source_entry.get()
    dest_dir = destination_entry.get()
    shutil.copy(os.path.join(source_dir, selected_file), dest_dir)
    refresh_file_list()

# Function to cut selected file
def cut_file():
    selected_file = file_listbox.get(tk.ACTIVE)
    source_dir = source_entry.get()
    dest_dir = destination_entry.get()
    shutil.move(os.path.join(source_dir, selected_file), dest_dir)
    refresh_file_list()

# Function to refresh file list
def refresh_file_list():
    source_dir = source_entry.get()
    file_listbox.delete(0, tk.END)
    for filename in os.listdir(source_dir):
        file_listbox.insert(tk.END, filename)

# Function to organize files
def organize():
    source_dir = source_entry.get()
    organize_files(source_dir)
    refresh_file_list()

# Create the main application window
root = tk.Tk()
root.geometry("500x350")
root.title("File Organizer")

# Source directory entry
source_label = tk.Label(root, text="Source Directory:",)
source_label.grid(row=0, column=0, sticky="w")
source = tk.StringVar()
global source_entry
source_entry = tk.Entry(root, width=50, textvariable=source, bg="pink")
source_entry.grid(row=0, column=1, padx=5, pady=5)

# Destination directory entry
destination_label = tk.Label(root, text="Destination Directory:")
destination_label.grid(row=1, column=0, sticky="w")
global dest_vari
dest_vari = tk.StringVar()
destination_entry = tk.Entry(root, width=50, textvariable= dest_vari, bg="pink")
destination_entry.grid(row=1, column=1, padx=5, pady=5)

# File listbox
file_listbox = tk.Listbox(root, width=70, height=15)
file_listbox.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Buttons
copy_button = tk.Button(root, text="Copy", command=copy_file, bg="#e4e866")
copy_button.place(x=20, y=320)

cut_button = tk.Button(root, text="Cut", command=cut_file, bg="#e4e866")
cut_button.place(x=370, y=320)

organize_button = tk.Button(root, text="Organize Files", command=organize, bg="#e4e866")
organize_button.place(x=170, y=320)


def the_browse():
    temp = str(filedialog.askdirectory())
    source_entry.insert(1, temp)


#browse button
browse = tk.Button(root, text="Browse", command=the_browse, bg="#66b5c4")
browse.place(x=440, y=2)


# Main loop
root.mainloop()
