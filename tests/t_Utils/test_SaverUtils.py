from src.Utils.SaverUtils import Saver
from src.Utils.Loader import Loader

import os.path
import pytest
import pandas as pd

from os import path
TABLE_PATH = "/Users/yigitbaser/Coronavirusmodel/Storage/TestData/TotalTable_77.csv"

TEST_FILE_1 = "/Users/yigitbaser/Coronavirusmodel/Storage/TestData/TempData/TotalTable_1933.csv"
TEST_FILE_2 = "/Users/yigitbaser/Coronavirusmodel/Storage/TestData/TempData/TotalTable_1932.csv"

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

#@pytest.mark.parametrize('input_files',[ TEST_FILE_1,
    #                               TEST_FILE_2
#], ids=repr)
@pytest.mark.parametrize('saved_files',[ TEST_FILE_1,
                                   TEST_FILE_2
], ids=repr)
def test_save_to_directory(saved_files):
    """

    """
    if os.path.exists(saved_files):
        os.remove(saved_files)

    data_to_save = Loader.load_data(file_path=TABLE_PATH)
    Saver.save_to_directory(data_to_save=data_to_save, directory=saved_files)
    assert path.exists(saved_files) == True






