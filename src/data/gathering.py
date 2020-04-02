"""
Gathers data from www.worldometers.info

"""
import pandas as pd
import requests


URL_GENERAL_DATA = 'http://www.worldometers.info/coronavirus'
URL_AGE_SEX_DATA = 'http://www.worldometers.info/coronavirus/coronavirus-age-sex-demographics/'
URL_DEATH_TOLL = 'http://www.worldometers.info/coronavirus/coronavirus-death-toll/'

class gathering():
    """
    Contains functions to get data from website
    """
    def __init__(self):
        definition = ""

    def run(data_type:str) -> pd.DataFrame:
        """
        #TODO DESIGN IT
        Runs  functions
        :param data_type:
        :return:
        """
        if data_type == "TotalTable":
            return gathering.get_total_data()
        elif data_type == "DataAge":
            return gathering.get_age_data()
        elif data_type == "DataSex":
            return gathering.get_sex_data()
        elif data_type == "DataPrecon":
            return gathering.get_precondition_data()
        elif data_type == "DataTotalDeaths":
            return gathering.get_total_deaths_data()
        elif data_type == "DataDailyDeaths":
            return gathering.get_daily_deaths_data()


    def read_avoid_403(url: str) -> pd.DataFrame:
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        r = requests.get(url, headers=header)
        return pd.read_html(r.text)

    def get_total_data(url:str=URL_GENERAL_DATA) -> pd.DataFrame:
        """
        Returns the main table imported from worldometers.
        :return: DataFrame.
        """
        ncov_data_cases = gathering.read_avoid_403(url)
        return ncov_data_cases[0]


    def get_age_data(url:str=URL_AGE_SEX_DATA) -> pd.DataFrame:
        """
        Returns death rate by age distribution
        :return: DataFrame. Age/DeathRate(ConfirmedCases)/DeathRate(AllCases)
        """
        ncov_data_age = gathering.read_avoid_403(url)
        return ncov_data_age[0]

    def get_sex_data(url:str = URL_AGE_SEX_DATA) -> pd.DataFrame:
        """
        Returns death rate by sex(male/female)
        :return: DataFrame. Sex/DeathRate(ConfirmedCases)/DeathRate(AllCases)
        """
        ncov_data_sex = gathering.read_avoid_403(url)
        return ncov_data_sex[1]

    def get_precondition_data(url:str=URL_AGE_SEX_DATA) -> pd.DataFrame:
        """
        Returns death rate by precondition(male/female)
        :return: DataFrame. PreexistingCondition/DeathRate(ConfirmedCases)/DeathRate(AllCases)
        """

        ncov_data_precon = gathering.read_avoid_403(url)
        return ncov_data_precon[2]

    def get_total_deaths_data(url:str= URL_DEATH_TOLL) -> pd.DataFrame:
        """
        Returns total death and daily change per day
        :return: DataFrame. Date/TotalDeath/ChangeInTotal/ChangeInTotal%
        """
        td_data = gathering.read_avoid_403(url)
        return td_data[0]

    def get_daily_deaths_data(url:str=URL_DEATH_TOLL) -> pd.DataFrame:
        """
        Returns daily death and change of it compared to day before
        :return: DataFrame. Date/DailyDeath/ChangeInDaily/ChangeInDaily%
        """
        td_data = gathering.read_avoid_403(url)
        return td_data[1]
