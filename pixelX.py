import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image
import os
import threading
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_images_to_pdf(image_folder, output_pdf, progress_var):
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
    if not image_files:
        status_label.config(text="No image files found in the folder.")
        return

    total_images = len(image_files)
    progress_step = 100 / total_images

    progress = 0

    c = canvas.Canvas(output_pdf, pagesize=letter)

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        try:
            img = Image.open(image_path)
            img_width, img_height = img.size
            aspect_ratio = img_width / img_height
            pdf_width, pdf_height = letter
            pdf_height = pdf_width / aspect_ratio
            c.setPageSize((pdf_width, pdf_height))
            c.drawImage(image_path, 0, 0, pdf_width, pdf_height)
            c.showPage()
        except Exception as e:
            print(f"Failed to process {image_file}: {str(e)}")

        progress += progress_step
        progress_var.set(progress)

    c.save()
    status_label.config(text=f"PDF file '{output_pdf}' created successfully.")
    enable_buttons()

def compress_images(image_folder, quality, progress_var):
    total_files = sum(1 for filename in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, filename)) and filename.lower().endswith(('.jpg', '.jpeg', '.png')))
    progress_step = 100 / total_files

    progress = 0
    for filename in os.listdir(image_folder):
        filepath = os.path.join(image_folder, filename)
        if os.path.isfile(filepath) and filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            img = Image.open(filepath)
            new_filepath = os.path.splitext(filepath)[0] + '_compressed' + os.path.splitext(filepath)[1]
            img.save(new_filepath, quality=quality)
            progress += progress_step
            progress_var.set(progress)
    status_label.config(text="Compression completed.")
    enable_buttons()

def select_folder_and_convert():
    if not task_running.get():
        default_download_folder = os.path.expanduser("~/Downloads")
        folder_path = filedialog.askdirectory(initialdir=default_download_folder)
        folder_name = os.path.basename(folder_path)
        if folder_path:
            output_pdf = os.path.join(folder_path, f"{folder_name}.pdf")
            progress_var.set(0)
            disable_buttons()
            threading.Thread(target=convert_images_to_pdf, args=(folder_path, output_pdf, progress_var)).start()

def select_folder_and_compress():
    if not task_running.get():
        default_download_folder = os.path.expanduser("~/Downloads")
        folder_path = filedialog.askdirectory(initialdir=default_download_folder)
        if folder_path:
            quality = int(quality_slider.get())
            progress_var.set(0)
            disable_buttons()
            threading.Thread(target=compress_images, args=(folder_path, quality, progress_var)).start()

def disable_buttons():
    convert_button.config(state=tk.DISABLED)
    compress_button.config(state=tk.DISABLED)
    task_running.set(True)

def enable_buttons():
    convert_button.config(state=tk.NORMAL)
    compress_button.config(state=tk.NORMAL)
    task_running.set(False)

def update_quality_label(value):
    quality_label.config(text=f"Compression Quality: {round(float(value))}")
    
# Create GUI
root = tk.Tk()
root.title("PixelX: Image Converter and Compressor v0.0.1")
root.geometry('600x220+400+200')
root.resizable(False, False)
task_running = tk.BooleanVar()
task_running.set(False)

convert_button = tk.Button(root, text="Convert to PDF", command=select_folder_and_convert)
convert_button.pack(pady=10)

compress_button = tk.Button(root, text="Compress Images", command=select_folder_and_compress)
compress_button.pack(pady=10)

quality_frame = tk.Frame(root)
quality_frame.pack()

quality_label = tk.Label(quality_frame, text="Compression Quality: 100")
quality_label.pack(side=tk.LEFT)

quality_slider = ttk.Scale(quality_frame, from_=0, to=100,
                           orient=tk.HORIZONTAL, command=update_quality_label)
quality_slider.set(100)  # Set default value to 100
quality_slider.pack(side=tk.LEFT, padx=10)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=200, mode='determinate', variable=progress_var)
progress_bar.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

author_label = tk.Label(root, text="Author: Leo N (@nphausg) 2024", anchor=tk.NE)
author_label.pack(side=tk.RIGHT, padx=10, pady=0)

root.mainloop()
