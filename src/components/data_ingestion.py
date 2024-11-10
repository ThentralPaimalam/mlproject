import os
# when working as a Data scientist we need to have seprate a team called 
# big data team so we need to know how to read data from specific data source like local data source,or mongodb ,sql and so on
# here we split the data and then do the transformation
import pandas as pd
from sklearn.model_selection import train_test_split
import sys# import sys for custom exception 
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass #for creating class variable



# input are required to know where to save the training data ,testing data due to which we use class datainjectionconfig
@dataclass  #defining the class variable directly called decorator
class DataIngestionConfig: 
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

# now dataIngestionConfig know where to store the csv file since pathe is defined by using os.path in the folder named artifacts

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

#Once DataIngestion class is being called  that three parts in DataIngestionConfig() will be initialized to the class variable ingestion_config
    
    def initiate_data_ingestion(self):  #used for reading the data from any data source like mongodb or sql
        logging.info("Enter data ingestion method")
        try:
            df = pd.read_csv(r"C:\mlproject\src\notebook\data\stud.csv") #right now im reading it from local data source 
            logging.info("Read the dataset as dataframe")#have a practice of writing the log bcoz its easy to track the exception
            #lets create directory for all three file with same folder
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok =True)
 
            df.to_csv(self.ingestion_config.raw_data_path,index =False,header =True)

            logging.info("Train Test split intiated")
            train_set,test_set =train_test_split(df,test_size =0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index =False,header =True)
            test_set.to_csv(self.ingestion_config.test_data_path,index =False,header =True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )   #if i pass this 3 data it will be easy for the transformation to use
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()