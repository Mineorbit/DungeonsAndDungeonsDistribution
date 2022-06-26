from datetime import datetime

import aiofiles
import fastapi
from aiofiles import os
import os.path
from os import path

from starlette.responses import FileResponse


async def upload_file(in_file: fastapi.UploadFile):
    file_location = "library_files/Library.zip"
    async with aiofiles.open(file_location, 'wb') as out_file:
        content = await in_file.read()  # async read
        await out_file.write(content)

    return "Great Success, very nice"



async def download_file():
    return FileResponse("library_files/Library.zip", media_type="application/zip", filename="Library.zip")

