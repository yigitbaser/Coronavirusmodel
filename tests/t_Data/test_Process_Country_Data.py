import pytest
from src.Utils.Loader import Loader
from src.Data import Process_Country_Data

REAL_DATA_PATH = "/Users/yigitbaser/Coronavirusmodel/Storage/RealData/Stats_by_Country/Turkey/ActiveCases.csv"
@pytest.mark.parametrize("date",["2020-03-14",
                             "2020-03-21"
                             "2020-03-06",
                             "2020-03-30"])
def test_data():

    data_table=  Loader.load_data(file_path=REAL_DATA_PATH,index_col_pass=0)
    assert  data_table[data_table['ActiveCases'] == ]
