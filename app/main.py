from fastapi import FastAPI
from dotenv import load_dotenv
import os

import uvicorn

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "hi"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT")))
