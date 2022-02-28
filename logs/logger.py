import os
import logging

log_dir = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), 'logs')
log_file_name = os.path.join(log_dir, 'log_text.log')

logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler(log_file_name)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s.%(funcName)s - %(message)s')

fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.setLevel(logging.INFO)


if __name__ == "__main__":
    logger.info("LOGGER IS INITIALIZED...")
