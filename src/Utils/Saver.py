from pandas import Timestamp

from src.Data import gathering as gt


def save_to_db(get_fcn, data_type:str)
    time_now = Timestamp.now()
    time_date = Timestamp.date(time_now)
    table_name =



if __name__ == '__main__':
    time_now = Timestamp.now()
    time_date = Timestamp.date(time_now)

    DATA_TO_IMPORT = {'TotalTable', 'Data_Age', 'Data_Sex', 'Data_Precondition', 'Data_TotalDeath','Data_DailyDeath'}


    #Total Data
    data_total = gt.gathering.get_total_data()
    data_total['TimeStamp'] = time_now

    TABLE_TYPE = 'TotalTable'
    data_total.to_csv(
        '/Users/yigitbaser/Coronavirusmodel/Storage/'+ str(time_date)+'/'+TABLE_TYPE+'_'+str(time_now.hour)+str(
            time_now.minute) + '.csv')

    #Data Age

    data_age = gt.gathering.get_age_data()
    data_age['TimeStamp'] = time_now

    TABLE_TYPE = 'DATAAGE'
    data_age.to_csv(
        '/Users/yigitbaser/Coronavirusmodel/Storage/' + str(time_date) + '/' + TABLE_TYPE + '_' + str(
            time_now.hour) + str(
            time_now.minute) + '.csv')

    #Data Sex

    data_sex = gt.gathering.get_sex_data()
    data_sex['TimeStamp'] = time_now

    TABLE_TYPE = 'DATASEX'
    data_sex.to_csv(
        '/Users/yigitbaser/Coronavirusmodel/Storage/' + str(time_date) + '/' + TABLE_TYPE + '_' + str(
            time_now.hour) + str(
            time_now.minute) + '.csv')

    #Data Precondition

    data_precon = gt.gathering.get_precondition_data()
    data_precon['TimeStamp'] = time_now

    TABLE_TYPE = 'DATAPRECON'
    data_precon.to_csv(
        '/Users/yigitbaser/Coronavirusmodel/Storage/' + str(time_date) + '/' + TABLE_TYPE + '_' + str(
            time_now.hour) + str(
            time_now.minute) + '.csv')

    #Data Total Deaths
    data_total_death = gt.gathering.get_total_deaths_data()
    data_total_death['TimeStamp'] = time_now

    TABLE_TYPE = 'DATATOTALDEATH'
    data_total_death.to_csv(
        '/Users/yigitbaser/Coronavirusmodel/Storage/' + str(time_date) + '/' + TABLE_TYPE + '_' + str(
            time_now.hour) + str(
            time_now.minute) + '.csv')

    #Data Daily Deaths

    data_daily_death = gt.gathering.get_daily_deaths_data()
    data_daily_death['TimeStamp'] = time_now

    TABLE_TYPE = 'DATADAILYDEATH'
    data_daily_death.to_csv(
        '/Users/yigitbaser/Coronavirusmodel/Storage/' + str(time_date) + '/' + TABLE_TYPE + '_' + str(
            time_now.hour) + str(
            time_now.minute) + '.csv')