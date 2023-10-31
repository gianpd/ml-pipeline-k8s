from utils import get_logger
logger = get_logger('InferenceLogger')

from fastapi import FastAPI

app = FastAPI()
logger.info('Inference script - STARTED')


@app.get("/")
async def root():
    logger.info('Inference> root GET asked')
    return {"root": "I'am root"}

