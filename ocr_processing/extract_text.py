import pytesseract
from PIL import Image
import requests
from io import BytesIO

def extract_text_from_image(image_url):
    # Fetch image from cloudinary using the url
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    
    # Extract text using pytesseract
    extracted_text = pytesseract.image_to_string(img)
    return extracted_text