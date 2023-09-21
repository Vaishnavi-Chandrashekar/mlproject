import os, sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass #@-decorator
class DataIngestionConfig: #constructor
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")
    raw_data_path = os.path.join("artifacts", "raw.csv")
  
#notebook\data\income_cleandata.csv  
    
class DataIngestion: #constructor
    def __init__(self): 
        self.ingestion_config = DataIngestionConfig()
        
        
    def initiate_data_ingestion(self):
        logging.info("data ingestion started")
        try:
            logging.info("data reading using pandas library from local system")
            df = pd.read_csv(os.path.join("notebook/data", "income_cleandata.csv"))
            logging.info("data reading completed")
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("data splitted into train and test")
            
            train_set, test_set = train_test_split(df, test_size = 0.2, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header = True)
            
            logging.info("Data Ingestion completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.info("error occured in data ingestion stage")
            raise CustomException(e, sys)
    
if __name__=="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
    
# src\components\data_ingestion.py