from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

def img_to_str(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='eng+ukr')
    return text
