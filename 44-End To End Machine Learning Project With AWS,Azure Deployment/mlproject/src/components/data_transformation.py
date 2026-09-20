import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function si responsible for data trnasformation
        
        '''
        try:
            numerical_columns = ["reading score", "writing score"]
            categorical_columns = [
                "gender",
                "race/ethnicity",
                "parental level of education",
                "lunch",
                "test preparation course",
            ]

            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]
            )

            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]

            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)

                ]


            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="math score"
            numerical_columns = ["reading score", "writing score"]

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
        
        
        
        
'''
================ DATA TRANSFORMATION EXPLANATION ================

Purpose:
- Converts raw data into a format suitable for Machine Learning.
- Handles missing values, categorical data, and feature scaling.

1. DataTransformationConfig
    - Stores the path where the preprocessing object will be saved.
    - File: artifacts/preprocessor.pkl


2. Numerical Columns
    - "reading score" and "writing score" are numerical features.
    - Missing values are filled using the median.
    - StandardScaler is used to scale the numerical values.


3. Categorical Columns
    - Gender, race/ethnicity, education, lunch, etc. are categorical features.
    - Missing values are filled using the most frequent value.
    - OneHotEncoder converts categories into numerical values.
    - StandardScaler(with_mean=False) scales the encoded data.


4. Pipeline
    - Pipeline combines multiple preprocessing steps together.

    Numerical Pipeline:
    Data → Median Imputation → Standard Scaling

    Categorical Pipeline:
    Data → Most Frequent Imputation → One-Hot Encoding → Scaling


5. ColumnTransformer
    - Applies the numerical pipeline to numerical columns.
    - Applies the categorical pipeline to categorical columns.

            ColumnTransformer
                    ↓
    ┌───────────────┬────────────────────┐
    │ Numerical     │ Categorical        │
    │ Pipeline      │ Pipeline           │
    └───────────────┴────────────────────┘


6. Read Train and Test Data
    - Reads train.csv and test.csv created during Data Ingestion.

    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)


7. Separate Features and Target

    Target:
    - "math score"

    Features:
    - All other columns.

    X = input/features
    y = target


8. fit_transform()
    - Used on training data.
    - Learns preprocessing rules and transforms the data.

    preprocessing_obj.fit_transform(train_data)


9. transform()
    - Used on test data.
    - Uses the rules learned from training data.

    preprocessing_obj.transform(test_data)


10. np.c_
    - Combines the processed features and target column together.

    np.c_[features, target]


11. save_object()
    - Saves the preprocessing object as a .pkl file.
    - This object can be reused later when making predictions.

    artifacts/preprocessor.pkl


12. Return
    - Returns:
        1. Processed training data
        2. Processed testing data
        3. Preprocessor file path


==================== DATA FLOW ====================

Raw Dataset
    ↓
Data Ingestion
    ↓
train.csv + test.csv
    ↓
Data Transformation
    ↓
Handle Missing Values
    ↓
Encode Categorical Data
    ↓
Scale Numerical Data
    ↓
Processed Train/Test Data
    ↓
Save preprocessor.pkl
    ↓
Model Training


==================== MAIN FUNCTIONS ====================

get_data_transformer_object()
→ Creates the preprocessing pipeline.

initiate_data_transformation()
→ Reads data, applies preprocessing, saves the preprocessor,
    and returns transformed train/test data.


Run after Data Ingestion:
The train.csv and test.csv generated by Data Ingestion
are passed to initiate_data_transformation().

===============================================================
'''


'''sys Python ka module hai. Iska use error kis file aur kis line par
    hua jaise information identify karne ke liye kiya ja sakta hai.
    
    "Take the error (e) and system information (sys),
    and create a custom error message with useful details."

And raise means that custom error ko actually throw/show karo.


fit       → Training data se rules/values learn karta hai
transform → Un learned rules ko data par apply karta hai


np.c_ → columns ke saath combine → side by side
np.r_ → rows ke saath combine    → one after another'''
