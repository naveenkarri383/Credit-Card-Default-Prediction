import os
from pathlib import Path  

project_name = "us_visa"

# Creating necessary files and folders 
list_of_files = [

    f"{project_name}/__init__.py",   # __init__ constructor
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py", # main application file 
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py", #testing the project
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml"
]

# Converting everything to folders and files
# backward slash "/" is used below that may works and sometimes errors may come based on using operating systems
for filepath in list_of_files:  
    filepath = Path(filepath) # converting into path
    # File director and file name
    filedir, filename = os.path.split(filepath)  # Split function is used so that seprate into folders and files
    if filedir != "": # Check file is there or not
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # Checking file is empty or not
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")
        