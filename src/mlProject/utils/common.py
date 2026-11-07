# /src/mlProject/utils/common.py

import logging
from pathlib import Path
from typing import Any
import yaml
from box import ConfigBox


# Logs handler setup
###################################################

# Project root: src/mlProject/utils/common.py -> project root
ROOT_DIR = Path(__file__).resolve().parents[3]
LOG_DIR = ROOT_DIR / "logs"

LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "history.log"

def get_logger(name: str) -> logging.Logger:
    """
    Create a logger that writes messages to both console and the log file.
    """

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False 
    
    # Prevents duplicate logs if multiple handlers are added.
    if not logger.handlers:
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s "
            "%(name)s: %(lineno)d - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Save logs to history.log file
        file_handler = logging.FileHandler(LOG_FILE,mode="a", encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Print logs to the terminal
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger


# Function for reading YAML files
def read_yaml(path: str | Path) -> ConfigBox:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"YAML configuration not found: {path}")
    with path.open("r", encoding="utf-8") as file:
        content = yaml.safe_load(file) or {}
    return ConfigBox(content)


# Function for creating directories
def create_directories(paths: list[str | Path]) -> None:
    for path in paths:
        Path(path).mkdir(parents=True, exist_ok=True)



# Function for saving JSON files
def save_json(data: dict[str, Any], path: str | Path) -> Path:
    import json
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    return path