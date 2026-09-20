import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # df=pd.read_csv('notebook\data\stud.csv')
            #df = pd.read_csv(r'notebook\data\stud.csv')
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

'''RUN Command :- python -m src.components.data_ingestion'''



'''
================ DATA INGESTION EXPLANATION ================

@dataclass
- Used to create a configuration class for storing file paths.

class DataIngestionConfig:
- Stores paths of raw, train, and test datasets.

train_data_path = 'artifacts/train.csv'
- Location where training data will be saved.

test_data_path = 'artifacts/test.csv'
- Location where testing data will be saved.

raw_data_path = 'artifacts/data.csv'
- Location where the original dataset will be saved.


class DataIngestion:
- Handles the complete data ingestion process.

self.ingestion_config = DataIngestionConfig()
- Creates the configuration object and gets all file paths.


#pd.read_csv(r'notebook\data\stud.csv')
#- Reads the original CSV dataset.
#- 'r' means raw string, so Windows '\' is treated correctly.

Use this :- pd.read_csv('notebook/data/stud.csv')


os.makedirs(..., exist_ok=True)
- Creates the artifacts folder if it does not already exist.


df.to_csv(...)
- Saves the original dataset into artifacts/data.csv.


train_test_split(df, test_size=0.2, random_state=42)
- Splits the dataset into:
    80% Training Data
    20% Testing Data
- random_state=42 keeps the split the same every time.


train_set.to_csv(...)
- Saves training data as artifacts/train.csv.


test_set.to_csv(...)
- Saves testing data as artifacts/test.csv.


return (train_data_path, test_data_path)
- Returns the locations of the train and test files.


try:
- Contains the main data ingestion code.


except Exception as e:
- Catches errors if something goes wrong.


raise CustomException(e, sys)
- Sends the error to the project's custom exception handler.


if __name__ == "__main__":
- Runs the code only when this Python file is executed directly.


obj = DataIngestion()
- Creates an object of the DataIngestion class.


obj.initiate_data_ingestion()
- Starts the complete data ingestion process.


==================== FLOW ====================

CSV Dataset
    ↓
Read Dataset
    ↓
Save Raw Data
    ↓
80/20 Train-Test Split
    ↓
Save train.csv + test.csv
    ↓
Ready for Data Transformation

Run:
python -m src.components.data_ingestion
================================================
'''


'''@dataclass is used to create classes that mainly store data, while automatically generating common methods like __init__().

So basically, @dataclass = less code + easy data/configuration management.'''