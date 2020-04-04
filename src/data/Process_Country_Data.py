"""
To process country data
"""
import numpy as np
import pandas as pd

from src.Utils.saver_utils import Saver

ACTIVE_CASES = np.array([1, 1, 1, 5, 6, 18, 47, 97, 189, 355, 661, 926,
                         1206, 1492, 1828, 2348, 3528, 5564, 7224, 8981, 10497,
                         13074, 15069, 17364], dtype=np.int)

DF_ACTIVE_CASES = pd.DataFrame(ACTIVE_CASES)

DF_ACTIVE_CASES.set_index(pd.to_datetime(np.arange(0, 50, 1), unit='D',
                                         origin=pd.Timestamp('2020-03-10'))[0:24], inplace=True)

ACTIVE_CASES_DIRECTORY = "/Users/yigitbaser/Coronavirusmodel/Storage/RealData/Stats_by_Country" \
                         "/Turkey/ActiveCases.csv"

DF_ACTIVE_CASES.columns = ['ActiveCases']
Saver.save_to_directory(data_to_save=DF_ACTIVE_CASES, directory=ACTIVE_CASES_DIRECTORY,
                        header_inp=True)


def create_data(data: np.ndarray, start_day: pd.Timestamp = '2020-03-10'):
    """
    NOT WRITTEN - TO CREATE DATA WITH DAYS AS INDEX
    :param directory:
    :param data:
    :param start_day:
    :return:
    """
    df_data = pd.DataFrame(data)
    df_data.set_index(pd.to_datetime(np.arange(df_data.size), unit='D',
                                     origin=pd.Timestamp(start_day))[0:24], inplace=True)
