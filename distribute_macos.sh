#!/bin/bash
rm -rf dist \;
pyinstaller --name 'pixelX' \
            --icon 'icon.png' \
            --add-data 'icon.png:.' \
            --add-data 'README.md:.' \
            --osx-bundle-identifier 'com.nphausg.images2pdf'\
            --windowed  \
            --onefile \
            pixelX.py