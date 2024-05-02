<h1 align="center"> Images to PDF Converter </h1>

<div align="center">
    <img src="https://img.shields.io/badge/python-v3.9-blue.svg">
</div>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)

## 👉 Overview

The Image to PDF Converter is a simple Python application that allows users to convert multiple images into a single PDF file. It provides a graphical user interface (GUI) built using the Tkinter library, making it easy for users to select a folder containing images and generate a PDF document from them. The application supports various image formats such as JPG, JPEG, PNG, GIF, and BMP. Additionally, it maintains the aspect ratio of the images within the PDF file to ensure accurate representation.

<img src="docs/cover.png"> 

### 🚀 Key Features:

- **Select Folder**: Users can select a folder containing images using a file dialog.

- **Convert Images**: The application converts all images in the selected folder into a single PDF document.

- **Maintain Aspect Ratio**: Images maintain their aspect ratio within the PDF file to preserve their original appearance.

- **Display Status**: The GUI displays status messages to inform users about the conversion process and the location of the generated PDF file.

- **Calculate Total Files Size**: Optionally, the application calculates and displays the total size of all files in the selected folder before converting them to PDF.

## 🚀 How to use

Cloning the repository into a local directory and checkout the desired branch:

```
git clone git@github.com:nphausg/images2pdf.git
git checkout master
source .venv/bin/activate
.venv/bin/python images2pdf.py
```
1. Run the Python script image_to_pdf_converter.py.
2. Click the "Select Folder" button to choose a folder containing images. Once a folder is selected, the application converts the images into a PDF file and displays the status message. *Optionally, users can view the total size of all files in the selected folder before conversion*.

## 🚀 Dependencies

- Python 3.x
- Tkinter
- reportlab
- Pillow

## 🍲 Screenshots

<h4 align="center">

<img src="docs/demo.png"> 


## ✨ Contributing

Contributions to this project are welcome. Feel free to submit issues, suggest improvements, or create pull requests.

## ✨ Acknowledgments:
Special thanks to the developers of the Tkinter, reportlab, and Pillow libraries for providing the tools necessary to build this application.


## 👀 Author

<p>
    <a href="https://nphausg.medium.com" target="_blank">
    <img src="https://avatars2.githubusercontent.com/u/13111806?s=400&u=f09b6160dbbe2b7eeae0aeb0ab4efac0caad57d7&v=4" width="96" height="96">
    </a>
</p>
