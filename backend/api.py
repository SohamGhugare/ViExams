from fastapi import FastAPI, File, UploadFile
import uvicorn
from utils import OcrUtility
from webhook import WebhookHandler
wh_handler = WebhookHandler()

app = FastAPI(
    title="ViExams API",
    debug=True
)

@app.get("/api/papers")
async def fetch_papers(limit: int=5, course: str=None):
    return {"data": "root"}

@app.post("/api/upload")
async def upload_image(file: UploadFile = File()):

    contents = file.file.read()
    img_path = f"backend/cache/{file.filename}"
    with open(img_path, "wb") as f:
        f.write(contents)

    wh_url = "https://discord.com/api/webhooks/1081793607926816808/BzjWmFl3D1fkftDM50A_J2Ek-M8oP4BOJPB5TqlpgzrSxUnFajBug0ynYwTJaxGrc1JY"
    await wh_handler.send_webhook(webhook_url=wh_url, image_path=img_path)
    

    return {"response": {
        "status": 200,
        "data": "Successfully Uploaded!"
    }}
                                                                                                

if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)