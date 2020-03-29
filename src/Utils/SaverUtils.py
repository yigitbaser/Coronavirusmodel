import pandas as pd
from pandas import Timestamp

from src.Data import gathering as gt


class Saver():
    DATA_TO_IMPORT = {'TotalTable', 'Data_Age', 'Data_Sex', 'Data_Precondition', 'Data_TotalDeath',
                      'Data_DailyDeath'}
    def __init__(self, data:str, data_type:str, fcn, directory):
        self.DATA_ = data
        self.data_type = data_type
        self.function = fcn
        self.directory = directory

    def add_Timestamp(data_input: pd.DataFrame) -> pd.DataFrame:
        """
        This functions adds Tİmestamp as a column to DataFrame input
        :param data_input: DataFrame. Input data
        :return: DataFrame. Timestamped dataframe
        """
        data_input['Timestamp'] = Timestamp.now()
        return data_input

    def save_to_directory(self, data: pd.DataFrame, directory):
        return data.to_csv(directory+'.csv')

#    def save_all(self,directory):
#
 #       for table in self.DATA_TO_IMPORT:
 #           if table = 'TotalTable':
  #              data_table= gt.gathering.get_total_data()
  #              save_to_directory(data_table)

