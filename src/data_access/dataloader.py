import pandas as pd
import sys
import os
from src.exception import CustomException

class DataLoader:
    def __init__(self,data_dir):
        try:
            self.data_dir = data_dir
        except Exception as e:
            raise CustomException(e, sys)

    def load_csv(self,filename) -> pd.DataFrame:

        try:
            file_path = "C:\Users\123\Desktop\thyro-care\notebook\thyroid_cleaned_data.csv"
            return pd.read_csv(file_path)
        
        except Exception as e:
            raise CustomException(e, sys)