from fastapi import FastAPI, File, UploadFile
import uvicorn
from ocr import OCR


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

    contents = file.file.read()
    with open(f"backend/cache/{file.filename}", "wb") as f:
        f.write(contents)

    return {"data": "Successfully uploaded image!", "status": 200}
    

if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)