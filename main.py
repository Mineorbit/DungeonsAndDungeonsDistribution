from typing import Union

from fastapi import FastAPI
from fastapi import APIRouter, File, UploadFile
import shutil
import controllers as file_controller
app = FastAPI()
from io import BytesIO
import os

@app.get("/")
def read_root():
    return {"Hey :)"}


@app.post("/library", tags=["library"])
async def upload_library(file: UploadFile = File(...)):
    file = await file_controller.upload_file(file)
    return "Completed"


#https://www.tutorialsbuddy.com/how-to-zip-multiple-files-in-python-for-download-using-fastapi origin

@app.get("/library/build", tags=["library"])
async def build_library():
        os.remove("library_files/Library.zip")
        shutil.make_archive("library_files/Library", 'zip', "library_files/Library")
        return "Built Library Archive"




@app.get("/library", tags=["library"])
async def download_library():
    f = await file_controller.download_file()
    return f