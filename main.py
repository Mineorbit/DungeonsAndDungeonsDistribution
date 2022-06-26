from typing import Union

from fastapi import FastAPI
from fastapi import APIRouter, File, UploadFile
import controllers as file_controller
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/library", tags=["file"])
async def upload_library(file: UploadFile = File(...)):
    file = await file_controller.upload_file(file)
    return "Completed"


@app.get("/library", tags=["file"])
async def download_library():
    f = await file_controller.download_file()
    return f