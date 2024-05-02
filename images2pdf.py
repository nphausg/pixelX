import os
import platform
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog
import threading

from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def _format_size(size):
    # Convert size to human-readable format
    for unit in ['', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024


def convert_images_to_pdf(image_folder, output_pdf, progress_callback):
    # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(
        ('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

    if not image_files:
        print("No image files found in the folder.")
        return
    total_images = len(image_files)
    total_size = 0
    # Sort the image files by file name
    image_files = sorted(image_files)
    progress = 0
    # Create a new PDF file
    c = canvas.Canvas(output_pdf, pagesize=letter)

    # Loop through each image and add it to the PDF
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        total_size += os.path.getsize(image_path)
        try:
            img = Image.open(image_path)
            img_width, img_height = img.size
            aspect_ratio = img_width / img_height
            pdf_width, pdf_height = letter
            pdf_height = pdf_width / aspect_ratio  # Adjusting height based on aspect ratio
            c.setPageSize((pdf_width, pdf_height))
            c.drawImage(image_path, 0, 0, pdf_width, pdf_height)
            c.showPage()
        except Exception as e:
            print(f"Failed to process {image_file}: {str(e)}")

        progress += 1
        print(f"PDF file {progress} is in processing ...")
        progress_callback(progress, total_images, total_size)
    c.save()
    print(f"PDF file '{output_pdf}' created successfully.")
    return total_size

def select_folder():
    default_download_folder = os.path.expanduser("~/Downloads")
    folder_path = filedialog.askdirectory(initialdir=default_download_folder)
    folder_name = os.path.basename(folder_path)
    output_pdf = os.path.join(folder_path, f"{folder_name}.pdf")
    status_label.config(text="Converting images...")
    def update_progress(progress, total_images, total_size):
        progress_percent = (progress / total_images) * 100
        status_label.config(text=f"Converting images... {progress}/{total_images} ({progress_percent:.2f}%)")
        if progress_percent == 100:
            # Convert total size to human-readable format
            total_size_str = _format_size(total_size)
            status_label.config(text=f"Selected folder: {folder_name}\n{total_images} PDF file(s) ({total_size_str}) have been merged successfully into\n'{output_pdf}'.")
            # Open the folder containing the PDF file
            if platform.system() == "Windows":
                os.startfile(folder_path)
            else:
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, folder_path])
    threading.Thread(target=convert_images_to_pdf, args=(folder_path, output_pdf, update_progress)).start()
# Create GUI
root = tk.Tk()
root.geometry("800x200")
# Load the image file from disk.
icon = tk.PhotoImage(file="icon.png")
# Set it as the window icon.
root.iconphoto(True, icon)

root.title("Images to PDF Converter")

select_folder_button = tk.Button(root, text="Select Folder", command=select_folder)
select_folder_button.pack(pady=20)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
