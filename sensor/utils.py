import pandas as pd
from sensor.logger import logging
from sensor.exception import SensorException
# from sensor.config import mongo_client
import os,sys
import yaml
FILEPATH = 'F:\aps-fault-detection\aps_dataset.csv'

def get_collection_as_dataframe()->pd.DataFrame:
    """
    return Pandas dataframe of a collection
    """
    FILEPATH = 'aps_dataset.csv'

    try:
        logging.info(f"Reading the data from the {FILEPATH} and converting in dataframe.")
        df = pd.read_csv(FILEPATH)
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id ")
            df = df.drop("_id",axis=1)
        logging.info(f"Row and columns in df: {df.shape}")
        return df
    except Exception as e:
        raise SensorException(e, sys)



def write_yaml_file(file_path,data:dict):
    try:
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir,exist_ok=True)
        with open(file_path,"w") as file_writer:
            yaml.dump(data,file_writer)
    except Exception as e:
        raise SensorException(e, sys)

def convert_columns_float(df:pd.DataFrame,exclude_columns:list)->pd.DataFrame:
    try:
        for column in df.columns:
            if column not in exclude_columns:
                df[column]=df[column].astype('float')
        return df
    except Exception as e:
        raise e
    

def convert_columns_float(df:pd.DataFrame,exclude_columns:list)->pd.DataFrame:
    try:
        for column in df.columns:
            if column not in exclude_columns:
                df[column]=df[column].astype('float')
        return df
    except Exception as e:
        raise e