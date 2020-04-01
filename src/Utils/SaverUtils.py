import pandas as pd
from pandas import Timestamp

from src.Data import gathering as gt
DATA_TO_IMPORT = {'TotalTable', 'Data_Age', 'Data_Sex', 'Data_Precondition', 'Data_TotalDeath',
                      'Data_DailyDeath'}

class Saver():

    def __init__(self, data:str = None , data_type:str = None, fcn=None, directory:str = None):
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


#if __name__ == '__main__':

   # for data_type in DATA_TO_IMPORT:
    #    name = str(data_type)
     #       gt.gathering.get_total_data()


#    def save_all(self,directory):
#
 #       for table in self.DATA_TO_IMPORT:
 #           if table = 'TotalTable':
  #              data_table= gt.gathering.get_total_data()
  #              save_to_directory(data_table)

