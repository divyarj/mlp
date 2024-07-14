import logging
import os
import sys
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOF_FOLDER=f"{datetime.now().strftime('%m_%d_%Y')}"
logs_path=os.path.join(os.getcwd(), 'logs', LOF_FOLDER)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join('logs', LOF_FOLDER, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
