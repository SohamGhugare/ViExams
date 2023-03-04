from fastapi import FastAPI, File, UploadFile
import uvicorn
from utils import OcrUtility

app = FastAPI(
    title="ViExams API",
    debug=True
)

@app.get("/api/")
async def index():
    return {"data": "root"}

@app.post("/api/upload")
async def upload_image(file: UploadFile = File()):

    contents = file.file.read()
    with open(f"backend/cache/{file.filename}", "wb") as f:
        f.write(contents)

    course = OcrUtility().parse_course(f"backend/cache/{file.filename}")

    # return {"data": "Successfully uploaded image!", "status": 200}
    return {"response": {
        "status": 200,
        "data": "Successfully Uploaded!"
    }}
    

if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)