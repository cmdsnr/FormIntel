import pytesseract
from PIL import Image

def extract_text(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)