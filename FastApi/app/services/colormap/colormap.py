from fastapi import APIRouter,File, UploadFile
from typing import List
import os

from app.services.colormap.spec import Spec

router = APIRouter()

@router.post("/files")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@router.post("/files/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    UPLOAD_DIRECTORY = "./"
    for file in files:
        contents = await file.read()
        with open(os.path.join(UPLOAD_DIRECTORY, file.filename), "wb") as fp:
            fp.write(contents)
        print(file.filename)
    fname= [file.filename for file in files][0]
    return Spec.service(filename=fname)