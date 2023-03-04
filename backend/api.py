from fastapi import FastAPI, File, UploadFile
import uvicorn
from ocr import OCR
from io import BytesIO
import requests
from discord import File as DFile
from PIL import Image
import pytesseract

app = FastAPI(
    title="ViExams API",
    debug=True
)

ocr = OCR()

@app.get("/api/")
async def index():
    return {"data": "root"}

@app.post("/api/upload")
async def upload_image(file: UploadFile = File()):
    # contents = file.file.read()

    byt = BytesIO(requests.get("https://imgur.com/a/XZLb79k").content)
    contents = file.file.read()
    with open(file.filename, "wb") as f:
        f.write(contents)
    with open(file.filename, "rb") as f:    
        return {"data": f.read()}

if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)