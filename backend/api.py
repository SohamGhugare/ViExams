from fastapi import FastAPI
import uvicorn

app = FastAPI(
    debug=True
)

@app.get("/")
async def index():
    return {"data": "root"}

if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)