from src.Utils import SaverUtils
from src.Data.gathering import gathering as gt


if __name__ == '__main__':

    saver_obj = SaverUtils.Saver()

    for data_type in saver_obj.DATA_TO_IMPORT:
        if data_type == 'TotalData':
            data = gt.get_total_data()
            data.Saver.add_Timestamp()
            data.Saver.save_to_directory(da)


