#!/bin/bash
rm -rf dist \;
pyinstaller --name 'images2pdf' \
            --icon 'icon.png' \
            --add-data 'icon.png:.' \
            --add-data 'README.md:.' \
            --osx-bundle-identifier 'com.nphausg.images2pdf'\
            --windowed  \
            --onefile \
            images2pdf.py