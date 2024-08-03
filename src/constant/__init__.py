from datetime import datetime
import os

AWS_S3_BUCKET_NAME = "sensordeployment1"
#artifacts folder will be stored in this bucket

DATA_PATH = "C:\Users\123\Desktop\thyro-care\notebook\thyroid_cleaned_data.csv"
TARGET_COLUMN = "Recurred"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder_name = datetime.now().strftime("%m_%d_%Y_%H_%M_S")
artifact_folder = os.path.join("artifacts",artifact_folder_name)

# Ensure the local artifact folder exists
os.makedirs(artifact_folder, exist_ok=True)

# Define the path to save the model file
model_file_path = os.path.join(artifact_folder, MODEL_FILE_NAME + MODEL_FILE_EXTENSION)

print(f"Artifact folder: {artifact_folder}")
print(f"Model file path: {model_file_path}")