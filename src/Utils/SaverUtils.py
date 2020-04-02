# TODO Rename it to Saver
import pandas as pd
from pandas import Timestamp
import os.path
from src.Data import gathering as gt


class Saver():
    DATA_TO_IMPORT = {'TotalTable', 'DataAge', 'DataSex', 'DataPrecon', 'DataTotalDeaths',
                      'DataDailyDeaths'}

    def __init__(self, data: str = None, data_type: str = None, fcn=None, directory: str = None):
        self.data_ = data
        self.data_type = data_type
        self.fcn = fcn
        self.directory = directory

    def add_Timestamp(data_input: pd.DataFrame, timestamp_input: pd.Timestamp = None) -> pd.DataFrame:
        """
        #TODO add docstring to param timestamp
        #TODO If timestamp input has timestamp return EXCEPTION ALREADY TIMESTAMP EXCEPTION
        This functions adds Tİmestamp as a column to DataFrame input
        :param data_input: DataFrame. Input data
        :return: DataFrame. Timestamped dataframe
        """
        if timestamp_input == None:
            data_input['Timestamp'] = Timestamp.now()
        else:
            data_input['Timestamp'] = timestamp_input

        return data_input

    def check_directory(directory: str):
        if os.path.exists(directory):
            pass
        else:
            os.mkdir(directory)

    def save_to_directory(data_to_save: pd.DataFrame, directory: str):
            return data_to_save.to_csv(directory)

    # def
