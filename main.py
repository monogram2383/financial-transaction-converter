import logging

from fastapi import FastAPI, File, UploadFile, Response
import pandas as pd
from uvicorn import run

app = FastAPI()
logger = logging.getLogger(__name__)

@app.post("/process_privat24_transactions")
async def process_privat24_transactions(file: UploadFile = File(...)):
    logger.info(f"Privat24 transactions uploaded: {file.filename}")

    if file.content_type != "text/csv":
        return Response(status_code=415, media_type="application/json",
                        content=f"Unsupported file type: {file.content_type}. Provide a text/csv file.")

    df = pd.read_csv(file.file)
    print(df)
    return Response(status_code=200, media_type="application/json",
                    content="File {file.filename} uploaded successfully")


if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8000)
    logger.level = logging.DEBUG
    logger.info("Server started")
