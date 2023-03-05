import fitz 

class PdfToImage:
    def convert_to_img(self, pdf_path):
        with fitz.open(pdf_path) as pdf_doc:
            for page in pdf_doc:

                pix = page.get_pixmap()
                output_file = f'{pdf_path.split(".")[0]}-{page.number}.png'
                pix.save(output_file)

if __name__ == "__main__":
    PdfToImage().convert_to_img("backend/tests/chem-pdf.pdf")

