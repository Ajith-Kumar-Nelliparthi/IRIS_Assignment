import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


# project_name = "FastAPI-ML-Project"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"data/__init__.py",
    f"src/__init__.py",
    f"src/main.py",
    f"src/excel_processor.py",
    f"src/models.py",
    f"tests/__init__.py",
    f"tests/test_endpoints.py",
    "requirements.txt",
    "postman_collection.json",


]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")