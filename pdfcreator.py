from PIL import Image

image_1 = Image.open(r'/Users/nphau/Downloads/Visa Subclass 600/Tanh/Motorbike Registration Certificate/IMG_7075.jpg')
image_2 = Image.open(r'/Users/nphau/Downloads/Visa Subclass 600/Tanh/Motorbike Registration Certificate/IMG_7076.jpg')
im_1 = image_1.convert('RGB')
im_2 = image_2.convert('RGB')
image_list = [im_2]
im_1.save(r'file.pdf', save_all=True, append_images=image_list)
