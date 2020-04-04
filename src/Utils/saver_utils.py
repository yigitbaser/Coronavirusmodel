"""
Necessary fucntions to save the data from url as dataframe
"""

import os.path

import pandas as pd
from pandas import Timestamp


class Saver():
    """
    Class for necessary functions to save data
    """
    DATA_TO_IMPORT = {'TotalTable', 'DataAge', 'DataSex', 'DataPrecon', 'DataTotalDeaths',
                      'DataDailyDeaths'}

    def __init__(self, data: str = None, data_type: str = None, fcn=None, directory: str = None):
        self.data_ = data
        self.data_type = data_type
        self.fcn = fcn
        self.directory = directory

    @staticmethod
    def add_timestamp(data_input: pd.DataFrame, timestamp_input: pd.Timestamp = None) \
            -> pd.DataFrame:
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

    @staticmethod
    def create_directory(directory: str) -> bool:
        """
        Checks if directory exists
        :param directory:
        :return:
        """
        if not os.path.exists(directory):
            os.mkdir(directory)
            return True

    @staticmethod
    def save_to_directory(data_to_save: pd.DataFrame, directory: str, header_inp: bool = False):
        """
        To save the data to directory.
        :param data_to_save: pd.DataFrame. Data to save to the directory
        :param directory: str. Directory to write
        :param header_inp: If data has header
        :return:
        """
        return data_to_save.to_csv(path_or_buf=directory, header=header_inp)

    # def
