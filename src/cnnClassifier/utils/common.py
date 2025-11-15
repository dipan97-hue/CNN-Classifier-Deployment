import base64
import os
from box.exceptions import BoxValueError
import yaml
import json
from cnnClassifier import logger
import joblib
from ensure import ensure_annotations
from box import Configbox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path)-> Configbox:

    try:
        with open(path_to_yaml) as yml:
            content = yaml.safe_load(yml)
            logger.info(f"{path_to_yaml} is succefully loaded")
            return Configbox(content)
    except BoxValueError:
        logger.info("Not able to load")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
    
    if verbose:
        logger.info(f"{path_to_directories} has been created")

@ensure_annotations
def save_json(path: Path, data : dict):

    with open(path,'w') as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"{data} has been written to json path{path}")

@ensure_annotations
def load_json(path: Path)-> Configbox:

    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"Json file loaded into the {path}")

    return Configbox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):

    joblib.dump(data, filename= path)
    logger.info(f"binary file saved at {path}")

@ensure_annotations
def load_bin(path:Path) -> Any:

    data = joblib.load(path)

    logger.info(f"{data} loaded in the {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:

    size = round(os.path.getsize(path)/1024)

    logger.info(f"{size} KB")


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())



