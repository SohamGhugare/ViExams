"""
    This file contains all the utility code
"""

from ocr import OCR
from PIL import Image

class OcrUtility:
    def parse_course(self, img_path=None, content=None):
        if img_path:
            img = Image.open(img_path)
            extract = OCR().ocr(img)
            courses = [
                "Engineering Chemistry",
                "Calculus",
                "Basic Electrical and Electronics Engineering",
                "Engineering Physics",
                "Engineering Mechanics"
            ]
            for course in courses:
                if course in extract:
                    return course
                
if __name__ == "__main__":
    print(OcrUtility().parse_course(img_path="backend/tests/calculus-jpg.jpg"))

