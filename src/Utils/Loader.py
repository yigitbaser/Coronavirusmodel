"""
Stuff to load data
"""
from typing import Any

import pandas as pd


class Loader():
    """
    Load fucntions to load saved data
    """

    @staticmethod
    def load_data(file_path: str, index_col_pass: Any = None):
        """
        Loads the data in the given directory
        :param index_col_pass: check pandas read_csv
        :return: pd.Dataframe
        """
        data_frame = pd.read_csv(file_path, index_col=index_col_pass)
        return data_frame
