from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn
import random

from utils import OcrUtility
from webhook import WebhookHandler
wh_handler = WebhookHandler()

from database import Database
db = Database()

app = FastAPI(
    title="ViExams API",
    debug=True
)

@app.get("/api/papers")
async def fetch_papers(limit: int=5, course: str=None):
    links = db.fetch_links(course)
    if not links:
        raise HTTPException(
            status_code=404,
            detail="Course Not Found"
        )
    if len(links) > limit:
        l = []
        while len(l) < limit:
            item = random.choice(links)
            if item not in l:
                l.append(item)
    else:
        l = links.copy()

    return {"response": {
        "status": 200,
        "data": {
        "course": "random",
        "image_urls": l
        }
    }}

@app.post("/api/upload")
async def upload_image(file: UploadFile = File()):
    try:
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
    except:
        raise HTTPException(
            status_code=422,
            detail="Unprocessable Entity - Invalid Image Format / Non-parseable Image Uploaded"
        )
                                                                                                

if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)