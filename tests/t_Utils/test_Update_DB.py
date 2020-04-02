import os.path
#TODO FIX ALL FILE
from src.Data.gathering import gathering
from src.Utils.SaverUtils import Saver

#@pytest.fixture()
#def db(tmpdir):
    # GIVEN an empty db
 #   db_path = tmpdir.join("/Users/yigitbaser/Coronavirusmodel/Storage/TestData/TotalTable_77.csv")
 #   db = TasksDB(db_path)
 #   assert 0 == db.count()
#    yield db

directory = "/Users/yigitbaser/Coronavirusmodel/Storage/TestData/TempData/TotalTable_1933.csv"
TEST_FILE_2 = "/Users/yigitbaser/Coronavirusmodel/Storage/TestData/TempData/TotalTable_1932.csv"
def test_TotalData():

    total_data = get_total_data()
    total = Saver.add_Timestamp(total_data)
    Saver.save_to_directory(data_to_save=total, directory=directory)

    assert os.path.exists(directory) == True
def test_AgeData():
    age_data = get_total_data()
    total = Saver.add_Timestamp(age_data)
    Saver.save_to_directory(data_to_save=total, directory=directory)

