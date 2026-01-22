from fastapi import APIRouter, UploadFile, File
import shutil
import python_multipart
import pandas as pd


from models import *
from load_db import manager

router = APIRouter()

@router.post("/upload")
def upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    file.file.close()
    res = manager()
    return res










    

    

