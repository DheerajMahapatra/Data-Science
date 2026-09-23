import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException
from src.logger import logging

class TrainPipeline:
    def __init__(self):
        pass

    def start_training(self):
        try:
            logging.info("Training pipeline started")
            
            data_ingestion = DataIngestion()
            train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed. Train: {train_data_path}, Test: {test_data_path}")

            data_transformation = DataTransformation()
            train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
                train_data_path, test_data_path
            )
            logging.info(f"Data transformation completed. Preprocessor saved at: {preprocessor_path}")

            model_trainer = ModelTrainer()
            r2_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
            logging.info(f"Model training completed. R2 Score: {r2_score}")

            logging.info("Training pipeline completed successfully")
            return r2_score

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    train_pipeline = TrainPipeline()
    score = train_pipeline.start_training()
    print(f"Training completed with R2 Score: {score}")