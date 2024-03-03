from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\1612h\Tesseract-OCR\tesseract.exe"

result=pytesseract.image_to_string(Image.open("chap3/sample2.jpg"))
print(result)