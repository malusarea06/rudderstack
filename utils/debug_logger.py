import inspect
import sys
from pathlib import Path
import logging

IMPORT_PATH = Path("").absolute()
sys.path.append(str(IMPORT_PATH))

def set_debug_log(class_name):
    """
    Function to set logging for class
    """
    logger = logging.getLogger(class_name)
    logger.setLevel(logging.CRITICAL)
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(class_name, mode='a')
    formatter = logging.Formatter(
        "{asctime} : {name} : {levelname} : {message}",
        style='{',
        datefmt="%Y-%m-%d %H:%M"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger

def get_method_name():
    """
    Return method name of
    """
    try:
        return inspect.stack()[1][3]
    except IndexError:
        print("Issue with get method name funtion")
        return None
