from src.Utils.SaverUtils import Saver
from src.Data.Gathering import Gathering
import os
#TODO ADD CHECK FOLDER EXISTS IF NOT CREATE BY CURRENT DATE

if __name__ == '__main__':

    for data_imp in Saver.DATA_TO_IMPORT:
        directory_data  = "/Users/yigitbaser/Coronavirusmodel/Storage/RealData/02042020/" + data_imp + ".csv"

        Saver.save_to_directory(data_to_save=Saver.add_Timestamp(Gathering.run(data_type=data_imp)), directory=directory_data)




