from fastapi import APIRouter, UploadFile
import shutil
import python_multipart
import pandas as pd

from models import *
from load_db import *

router = APIRouter()

@router.post("upload")
def upload_file(file: UploadFile):
    if not file.filename.lower().endswith(('.csv',".xlsx",".xls")):
        return 404,"Please upload xlsx, or csv file."

    if file.filename.lower().endswith(".csv"):
        extension = ".csv"
    elif file.filename.lower().endswith(".xlsx"):
        extension = ".xlsx"

    filepath = "data/weapons_list"+ extension

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        if filepath.endswith(".csv"):
            df = pd.read_csv(filepath)
        else:
            df = pd.read_excel(filepath)
    except:
        return 401, "File is not proper"

    return df

def manager():
    df = load_csv()
    df = add_risk_level(df)
    df = clean_null(df)
    create_table(db, table_name)
    res = insert_df(df, table_name)
    return res











    

    

