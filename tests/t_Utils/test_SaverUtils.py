from src.Utils.SaverUtils import Saver
from src.Utils.Loader import Loader

import pandas as pd


TABLE_PATH = "/Users/yigitbaser/Coronavirusmodel/Storage/2020-03-22/TotalTable_77.csv"

def test_add_Timestamp():
    """
    Tests if added column is added then tests column 'Timestamp' includes timestamp objects.
    :return:
    """
    table_to_add = Loader.load_data(file_path=TABLE_PATH)
    added = Saver.add_Timestamp(data_input=table_to_add)
    assert 'Timestamp' in added.columns

    #Check if column 'Timestamp' contains df.Timestamp objects
    assert added['Timestamp'].dtype.str[1] == 'M'


def test_save_to_directory():
    """

    """
    pass




