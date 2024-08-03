import sys
import os
import numpy as np
import pandas as pd
from zipfile import Path
from dataclasses import dataclass
from src.exception import CustomException
from src.logging import logging

# logging.basicConfig() function in Python is used to configure the logging system. 
# Configure logging
logging.basicConfig(filename='../logs/data_ingestion.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')
artifact_folder = "../artifacts"

@dataclass
class DataIngestionConfig:
    #data_ingestion_dir:str means d_i_sir is expected to be a string
    data_ingestion_dir: str = os.path.join(artifact_folder, "data_ingestion")

    def initiate_data_ingestion(self) -> Path:
        """
            Method Name :   initiate_data_ingestion
            Description :   This method initiates the data ingestion components of training pipeline 
            
            Output      :   train set and test set are returned as the artifacts of data ingestion components
            On Failure  :   Write an exception log and then raise an exception
            
            Version     :   1.2
        """
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")
        os.makedirs(self.data_ingestion_dir, exist_ok=True)
        return Path(self.data_ingestion_dir)
    
    def read_data(file_path):
        # Read data from CSV file.
        try:
            data = pd.read_csv("C:\Users\123\Desktop\thyro-care\notebook\thyroid_cleaned_data.csv")
            logging.info(f"Data successfully read from {data}")
            return data
        except Exception as e:
            raise CustomException(e, sys) from e