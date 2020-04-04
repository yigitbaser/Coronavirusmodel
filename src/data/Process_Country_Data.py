from numpy.core._multiarray_umath import ndarray

from src.Utils.Loader import Loader
from src.Utils.SaverUtils import Saver
import numpy as np
import pandas as pd

active_cases = np.array([1, 1, 1, 5, 6, 18, 47, 97, 189,355,661,926,
                         1206,1492,1828,2348,3528,5564,7224,8981,10497,
                         13074,15069,17364], dtype=np.int)

df_active_cases = pd.DataFrame(active_cases)

df_active_cases.set_index(pd.to_datetime(np.arange(0, 50, 1), unit='D',
                                         origin=pd.Timestamp('2020-03-10'))[0:24],inplace=True)


active_cases_directory = "/Users/yigitbaser/Coronavirusmodel/Storage/RealData/Stats_by_Country/Turkey/ActiveCases.csv"

df_active_cases.columns = ['ActiveCases']
Saver.save_to_directory(data_to_save=df_active_cases, directory=active_cases_directory, header_inp=True)

def create_data(directory:str, data:np.ndarray,start_day:pd.Timestamp):
    df_data = pd.DataFrame(data)
    df_data.set_index(pd.to_datetime(np.arange(data.size), unit='D',
                                         origin=pd.Timestamp('2020-03-10'))[0:24],inplace=True)
