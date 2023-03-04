"""
    This file contains the OCR configurations
"""
from PIL import Image
import tika
from tika import parser

tika.initVM()

import pytesseract

class OCR:
    def ocr(self, image):
        return pytesseract.image_to_string(image=image)
        

    def run_tika(self):
        
        parsed_pdf = parser.from_file("backend/tests/chem-pdf.pdf")
        return parsed_pdf['contents']
    
    def run_test_ocr(self):
        image = Image.open("backend/tests/chem-jpg.jpg")
        return pytesseract.image_to_string(image=image)
    
if __name__ == "__main__":
    print(OCR().run_test_ocr())
    # print(OCR().run_tika())