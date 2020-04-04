"""
When you run it updates the data files in directory
"""
from src.Data.gathering import Gathering
from src.Utils.saver_utils import Saver

# TODO ADD CHECK FOLDER EXISTS IF NOT CREATE BY CURRENT DATE

if __name__ == '__main__':

    for data_imp in Saver.DATA_TO_IMPORT:
        directory_data = "/Users/yigitbaser/Coronavirusmodel/Storage/RealData/02042020/"\
                         + data_imp + ".csv"

        Saver.save_to_directory(data_to_save=Saver.add_timestamp(Gathering.run(data_type=data_imp)),
                                directory=directory_data)
