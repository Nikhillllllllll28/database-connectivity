import pytesseract
import PIL.Image
import cv2

myconfig = r"--psm 6 --oem 3"

text= pytesseract.image_to_string(PIL.Image.open("book.jpg"),config=myconfig)
print(text)