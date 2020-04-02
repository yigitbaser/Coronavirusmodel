"""
Tests for gathering.py
"""

import pytest
import os
import src.Utils.SaverUtils
from src.Data import Gathering

@pytest.mark.parametrize('input_type',[ 'TotalTable', 'DataAge', 'DataSex',
                                        'DataPrecon', 'DataTotalDeaths',
                                        'DataDailyDeaths'])
def test_gather_data(input_type):
    directory_data = "/Users/yigitbaser/Coronavirusmodel/Storage/TestData/TestGathering/" + input_type + ".csv"
    src.Utils.SaverUtils.Saver.save_to_directory(data_to_save=src.Utils.SaverUtils.Saver.add_Timestamp(Gathering.Gathering.run(data_type=input_type)), directory=directory_data)

    assert os.path.exists(directory_data) == True