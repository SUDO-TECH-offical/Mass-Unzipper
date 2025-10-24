import os
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox

def unzip_all_in_folder(folder_path):
    log_box.delete(1.0, tk.END)
    if not folder_path:
        messagebox.showerror("Error", "Please select a folder first!")
        return

    zip_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".zip"):
                zip_files.append(os.path.join(root, file))

    if not zip_files:
        messagebox.showinfo("No Files", "No zip files found in the selected folder.")
        return

    for zip_path in zip_files:
        try:
            extract_path = os.path.dirname(zip_path)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            os.remove(zip_path)
            log_box.insert(tk.END, f"✅ Unzipped and deleted: {zip_path}\n")
            log_box.see(tk.END)
        except Exception as e:
            log_box.insert(tk.END, f"❌ Error with {zip_path}: {e}\n")
            log_box.see(tk.END)

    messagebox.showinfo("Done", "All ZIP files processed!")

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder)

def start_unzip():
    folder = folder_entry.get()
    unzip_all_in_folder(folder)

root = tk.Tk()
root.title("Mass Unzipper 2000")
root.geometry("500x400")
root.config(bg="#d3d3d3")

title_label = tk.Label(root, text="Mass Unzipper - Made by @SUDO-TECH on tiktok", font=("Courier", 16, "bold"), bg="#d3d3d3")
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#c0c0c0", bd=2, relief="groove")
frame.pack(pady=10)

folder_label = tk.Label(frame, text="Folder:", bg="#c0c0c0")
folder_label.grid(row=0, column=0, padx=5, pady=5)
folder_entry = tk.Entry(frame, width=40)
folder_entry.grid(row=0, column=1, padx=5, pady=5)
browse_button = tk.Button(frame, text="Browse", command=select_folder, bg="#e0e0e0")
browse_button.grid(row=0, column=2, padx=5, pady=5)

start_button = tk.Button(root, text="Unzip Everything!", command=start_unzip, bg="#ffcc00", fg="black")
start_button.pack(pady=10)

log_box = tk.Text(root, width=60, height=12, bg="#f0f0f0", fg="black")
log_box.pack(padx=10, pady=10)

root.mainloop()
