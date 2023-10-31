from pathlib import Path

from fastapi import FastAPI

app = FastAPI()

TRAINING_LOGS_PATH = "./shared/training/logs"

@app.get("/")
async def root():
    return {"root": "I'am root\n"}

@app.get("/logs")
async def logs():
    # read logs from shared persistent volume
    pp = Path(TRAINING_LOGS_PATH)
    assert pp.exists(), f'{pp} does not exist.'
    log_file = list(map(lambda x: x, pp.glob('*.log')))[0]
    assert log_file, f'Not .log files present in {pp}'
    with open(log_file) as f:
        ff = f.read()
    
    return {'training_log': ff}
