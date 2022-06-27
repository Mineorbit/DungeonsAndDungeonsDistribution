from typing import Union

from fastapi import FastAPI
from fastapi import APIRouter, File, UploadFile
import shutil
import controllers as file_controller
app = FastAPI()
from io import BytesIO


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/library", tags=["file"])
async def upload_library(file: UploadFile = File(...)):
    file = await file_controller.upload_file(file)
    return "Completed"


#https://www.tutorialsbuddy.com/how-to-zip-multiple-files-in-python-for-download-using-fastapi origin

@app.get("/library/build")
async def build_library():
        shutil.make_archive(output_filename, 'zip', dir_name)
        return "Built Library Archive"




@app.get("/library", tags=["file"])
async def download_library():
    f = await file_controller.download_file()
    return f