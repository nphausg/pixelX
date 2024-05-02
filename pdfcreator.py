import tkinter as tk
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import platform, subprocess, sys
from PIL import Image
import os

def convert_images_to_pdf(image_folder, output_pdf):
        # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

    if not image_files:
        print("No image files found in the folder.")
        return 0

    # Sort the image files by file name
    image_files = sorted(image_files)

    # Create a new PDF file
    c = canvas.Canvas(output_pdf, pagesize=letter)

    # Loop through each image and add it to the PDF
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
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
    
    c.save()
    print(f"PDF file '{output_pdf}' created successfully.")
    return len(image_files)

def select_folder():
    default_download_folder = os.path.expanduser("~/Downloads")
    folder_path = filedialog.askdirectory(initialdir=default_download_folder)
    if folder_path:
        folder_name = os.path.basename(folder_path)
        output_pdf = os.path.join(folder_path, f"{folder_name}.pdf")
        num_of_files = convert_images_to_pdf(folder_path, output_pdf)
        status_label.config(text=f"Selected folder: {folder_name}\n{num_of_files} PDF file(s) have been merged successfully into '{output_pdf}'.")
     # Open the folder containing the PDF file
    if platform.system() == "Windows":
        os.startfile(folder_path)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, folder_path])

            
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