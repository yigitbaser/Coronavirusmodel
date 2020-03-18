"""
Gathers data from www.worldometers.info

"""
#TODO Write docstrings
import pandas as pd

URL_GENERAL_DATA = 'https://www.worldometers.info/coronavirus'
URL_AGE_SEX_DATA = 'https://www.worldometers.info/coronavirus/coronavirus-age-sex-demographics/'
URL_DEATH_TOLL = 'https://www.worldometers.info/coronavirus/coronavirus-death-toll/'

class gathering:
    """

    """
    def get_total_data() -> pd.DataFrame:
        """
        Returns the table imported from worldometers.
        :return: DataFrame.
        """
        ncov_data_cases = pd.read_html(URL_GENERAL_DATA)
        ncov_data_df = ncov_data_cases[0]
        return ncov_data_df

    def get_age_data() -> pd.DataFrame:
        """

        :return:
        """
        ncov_data_age = pd.read_html(URL_AGE_SEX_DATA)
        ncov_data_age_df = ncov_data_age[0]
        return ncov_data_age_df

    def get_sex_data() -> pd.DataFrame:
        ncov_data_sex = pd.read_html(URL_AGE_SEX_DATA)
        ncov_data_sex_df = ncov_data_sex[1]
        return ncov_data_sex_df

    def get_precondition_data() -> pd.DataFrame:
        ncov_data_precon = pd.read_html(URL_AGE_SEX_DATA)
        ncov_data_precon_df = ncov_data_precon[2]
        return ncov_data_precon_df

    def get_total_deaths_data():
        td_data = pd.read_html(URL_DEATH_TOLL)
        return td_data[0]

    def get_daily_deaths_data():
        td_data = pd.read_html(URL_DEATH_TOLL)
        return td_data[1]



    #print(NCOV_DATA_DF[NCOV_DATA_DF['Country,Other'] == 'Iran']['TotalCases'])



    #df[df['job']=='unemployed']['education'].value_counts()

    #df.to_csv('/Users/yigitbaser/Coronavirusmodel/dataCSV.csv', index=True)



    #t = ncov_data.pd.DataFrame.to_csv("data")
    #ncov_data.to_csv('/Users/yigitbaser/Coronavirusmodel', index=True)