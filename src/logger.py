import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import sys


logger = logging.getLogger(__name__)
def setup_logging(__name__):
    Path("logs").mkdir(exist_ok=True)
    logger.setLevel(logging.DEBUG)
    fmt = logging.Formatter("%(asctime)s %(levelname)s\t%(filename)s %(funcName)s - %(message)s")
    # File Handler
    file_handler = RotatingFileHandler("logs/provisioning.log", maxBytes=1024*1024*10, backupCount=3)
    # file_handler = logging.FileHandler("my_log.log")
    file_handler.setFormatter(fmt)
    file_handler.setLevel(logging.DEBUG)
    # Print Handler(STDOUT)
    print_handler = logging.StreamHandler(sys.stdout)
    print_handler.setLevel(logging.INFO)
    # Add Handlers
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(print_handler)
    return logger
