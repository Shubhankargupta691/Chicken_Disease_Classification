import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Change project name particular project name

project_name = "Chicken_Disease_Classification"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "main.py",
    "research/trials.ipynb",
    "research/data_ingestion.ipynb",
    "templates/index.html",

]

# Traverse the list of files one by one:

for filepath in list_of_files:
    filepath= Path(filepath)
    filedir, filename = os.path.split(filepath)

# Create directory if not exists:

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory; {filedir} for the file: {filename}")

# Create file insidde the  directories if not exists: 

    if( not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'Creating empty filee: {filepath}')

    else:
        logging.info(f"{filename} is already exists")