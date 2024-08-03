import sys
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logging import logging
from src.utils.main_utils import MainUtils
from dataclasses import dataclass

artifact_folder = "../artifacts"

@dataclass
class DataTransformationConfig:
    data_transformation_dir = os.path.join(artifact_folder, 'data_transformation')
    transformed_train_file_path = os.path.join(data_transformation_dir, 'train.npy')
    transformed_test_file_path = os.path.join(data_transformation_dir, 'test.npy')
    transformed_object_file_path = os.path.join(data_transformation_dir, 'preprocessing.pkl')

class DataTransformation:
    def __init__(self,
                 valid_data_dir):

        self.valid_data_dir = valid_data_dir

        self.data_transformation_config = DataTransformationConfig()

        self.utils = MainUtils()

    @staticmethod
    def get_merged_batch_data(valid_data_dir: str) -> pd.DataFrame:
        """
        Method Name :   get_merged_batch_data
        Description :  The get_merged_batch_data method reads all CSV files from a specified directory, 
        merges them into a single pandas DataFrame, and returns it.
        
        Output      :   a pandas DataFrame containing the merged data 
        On Failure  :   Write an exception log and then raise an exception
        
        Version     :   1.2
        Revisions   :   moved setup to cloud
        """
        try:
            raw_files = os.listdir(valid_data_dir) 
            #returns a list of all the file and directory names in the specified directory valid_data_dir.
            csv_data = []
            for filename in raw_files:
                data = pd.read_csv(os.path.join(valid_data_dir, filename))
                #reads the CSV file located at the specified path (valid_data_dir/filename) into a pandas DataFrame
                csv_data.append(data)

            merged_data = pd.concat(csv_data)
            return merged_data
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self):
        """
            Method Name :   initiate_data_transformation
            Description :   This method initiates the data transformation component for the pipeline 
            
            Output      :   data transformation artifact is created and returned 
            On Failure  :   Write an exception log and then raise an exception
            
        """
        logging.info("Entered initiate_data_transformation method of Data_Transformation class")

        try:
           dataframe = self.get_merged_batch_data(valid_data_dir=self.valid_data_dir)
           dataframe = self.utils.remove_unwanted_spaces(dataframe)
           X_train = dataframe.drop('Recurred', axis=1)
           y_train= dataframe['Recurred']
           #splitting data
           X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
           return X_train, y_train, X_test, y_test

        except Exception as e:
            raise CustomException(e, sys) from e
        
        ''' Data transformation refers to the process of converting data from one format or structure 
        into another to make it suitable for analysis or processing.'''