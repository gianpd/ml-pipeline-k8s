import os

import logging
import pathlib
from datetime import datetime
import logging.handlers as handlers

OUTPUT_FOLDER= os.environ['TRAINING_LOGS_PATH']
pathlib.Path(OUTPUT_FOLDER).mkdir(parents=True, exist_ok=True)

print('output path:')
print(OUTPUT_FOLDER)

def get_logger(name: str):
    fname = str(OUTPUT_FOLDER/pathlib.Path(f'{name}.log'))
    print(f'FNAME: {fname}')
    handler=[logging.handlers.TimedRotatingFileHandler(fname, utc=True, when='D', backupCount = 3)]
    logging.basicConfig(handlers=handler, level=logging.DEBUG, format = '%(name)s - %(asctime)s - %(levelname)s:    %(message)s')
    logger = logging.getLogger(name)    
    return logger