import os.path

import pytest
from src.Data.gathering import gathering
from src.Utils.SaverUtils import Saver

#@pytest.fixture()
#def db(tmpdir):
    # GIVEN an empty db
 #   db_path = tmpdir.join("/Users/yigitbaser/Coronavirusmodel/Storage/TestData/TotalTable_77.csv")
 #   db = TasksDB(db_path)
 #   assert 0 == db.count()
#    yield db

def test_TotalData():
    file_path = "/Users/yigitbaser/Coronavirusmodel/Storage/TestData/TotalTable_77.csv"

    total_data = gathering.get_total_data()
    total_data.add_Timestamp()
    total_data.save_to_directory(directory)

    pass

def test_Total():
    pass
    #assert os.path.exists("/Users/yigitbaser/Coronavirusmodel/Storage/2020-04-02/TotalData.csv")

