import pytesseract as pt
from PIL import Image

image = Image.open('D:/Program Files (x86)/Tesseract-OCR/1.jpg')

text = pt.image_to_string(image)

#print(text)