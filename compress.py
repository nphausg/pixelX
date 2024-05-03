import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image
import os
import threading


def compress_images(image_folder, quality, progress_var):
    total_files = sum(1 for filename in os.listdir(image_folder) if os.path.isfile(os.path.join(
        image_folder, filename)) and filename.lower().endswith(('.jpg', '.jpeg', '.png')))
    progress_step = 100 / total_files

    progress = 0
    for filename in os.listdir(image_folder):
        filepath = os.path.join(image_folder, filename)
        if os.path.isfile(filepath) and filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            img = Image.open(filepath)
            new_filepath = os.path.splitext(
                filepath)[0] + '_compressed' + os.path.splitext(filepath)[1]
            img.save(new_filepath, quality=quality)
            progress += progress_step
            progress_var.set(progress)
    status_label.config(text="Compression completed.")


def select_folder():
    default_download_folder = os.path.expanduser("~/Downloads")
    folder_path = filedialog.askdirectory(initialdir=default_download_folder)
    if folder_path:
        quality = quality_slider.get()
        progress_var.set(0)  # Reset progress bar
        threading.Thread(target=compress_images, args=(
            folder_path, quality, progress_var)).start()


def update_quality_label(value):
    quality_label.config(text=f"Compression Quality: {round(float(value))}")


# Create GUI
root = tk.Tk()
root.title("Image Compression")
root.resizable(False, False)
root.geometry('800x400+400+200')
select_folder_button = tk.Button(
    root, text="Select Folder", command=select_folder)
select_folder_button.pack(pady=20)

quality_frame = tk.Frame(root)
quality_frame.pack()

quality_label = tk.Label(quality_frame, text="Compression Quality: 100")
quality_label.pack(side=tk.LEFT)

quality_slider = ttk.Scale(quality_frame, from_=0, to=100,
                           orient=tk.HORIZONTAL, command=update_quality_label)
quality_slider.set(100)  # Set default value to 100
quality_slider.pack(side=tk.LEFT, padx=10)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(
    root, orient=tk.HORIZONTAL, length=200, mode='determinate', variable=progress_var)
progress_bar.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
