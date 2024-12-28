import logging

from fastapi import FastAPI, File, UploadFile, Response
from fastapi.responses import StreamingResponse, FileResponse
import pandas as pd
from uvicorn import run

from config import logger
from src.pipelines.pipeline_process_privat24_transactions import PipelineProcessPrivat24Transactions

app = FastAPI()

@app.post("/process_privat24_transactions")
async def process_privat24_transactions(input_file: UploadFile = File(...)):
    logger.info(f"[SYSTEM] Received Privat24 transactions: {input_file.filename}")

    if input_file.content_type != "text/csv":
        return Response(status_code=415, media_type="application/json",
                        content=f"Unsupported file type: {input_file.content_type}. Provide a text/csv file.")

    try:
        processed_transactions = PipelineProcessPrivat24Transactions.execute(file=input_file.file)
    except Exception as e:
        logger.error(f"[SYSTEM] Failed to execute privat24 transactions: {e}")
        return Response(status_code=500, media_type="application/json")

    logger.info(f"[SYSTEM] Successfully processed Privat24 transaction.")

    return StreamingResponse(
        iter([processed_transactions.to_csv(index=False)]),
        status_code=200,
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=data.csv"}
)


if __name__ == '__main__':
    run(app, host='0.0.0.0', port=9001)
    logger.level = logging.DEBUG
    logger.info("Server started")
