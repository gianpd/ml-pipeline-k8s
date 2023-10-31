"""
Training python script - start inside a container accessible from outside
"""

import time 
from utils import get_logger
logger = get_logger('train')

logger.info('Training started ...')
time.sleep(3)
logger.info('Training done.')


