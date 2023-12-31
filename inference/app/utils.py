import logging
import pathlib
from datetime import datetime
import logging.handlers as handlers

OUTPUT_FOLDER= './logs_folder'
pathlib.Path(OUTPUT_FOLDER).mkdir(exist_ok=True)

def get_logger(name: str):
    handler=[logging.handlers.TimedRotatingFileHandler(str(OUTPUT_FOLDER/pathlib.Path('inference.log')), utc=True, when='D', backupCount = 3)]
    logging.basicConfig(handlers=handler, level=logging.DEBUG, format = '%(name)s - %(asctime)s - %(levelname)s:    %(message)s')
    logger = logging.getLogger(name)    
    return logger