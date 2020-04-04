"""
Gathers data from www.worldometers.info

"""
import pandas as pd
import requests

from src.Exceptions import data_import_exception

URL_GENERAL_DATA = 'http://www.worldometers.info/coronavirus'
URL_AGE_SEX_DATA = 'http://www.worldometers.info/coronavirus/coronavirus-age-sex-demographics/'
URL_DEATH_TOLL = 'http://www.worldometers.info/coronavirus/coronavirus-death-toll/'


class Gathering():
    """
    Contains functions to get data from website
    """

    def __init__(self, data_type: str):
        """
        :type data_type: str.Type of data to use mainly in run(). For example, 'TotalTable'
        """
        self.data_type = data_type

    @staticmethod
    def run(data_type: str) -> pd.DataFrame:
        """
        #TODO DESIGN IT
        Runs  functions
        :param data_type:
        :return:
        """
        # TODO Fix here
        if data_type == "TotalTable":
            return Gathering.get_total_data()
        elif data_type == "DataAge":
            return Gathering.get_age_data()
        elif data_type == "DataSex":
            return Gathering.get_sex_data()
        elif data_type == "DataPrecon":
            return Gathering.get_precondition_data()
        elif data_type == "DataTotalDeaths":
            return Gathering.get_total_deaths_data()
        elif data_type == "DataDailyDeaths":
            return Gathering.get_daily_deaths_data()
        # TODO Exception
        else:
            raise data_import_exception.DataImportException()

    @classmethod
    def read_avoid_403(cls, url: str) -> pd.DataFrame:
        """
        Read the data from tables from url without having
        permission denied: 403 Error urllib
        :param self:
        :param url: str. url
        :return: Dataframe. Data on the url
        """
        # Open it like a browser
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        req = requests.get(url, headers=header)
        return pd.read_html(req.text)

    @staticmethod
    def get_precondition_data(url: str = URL_AGE_SEX_DATA) -> pd.DataFrame:
        """
        Returns death rate by precondition(male/female)
        :return: DataFrame. PreexistingCondition/DeathRate(ConfirmedCases)/DeathRate(AllCases)
        """

        ncov_data_precon = Gathering.read_avoid_403(url=url)
        return ncov_data_precon[2]

    @staticmethod
    def get_total_deaths_data(url: str = URL_DEATH_TOLL) -> pd.DataFrame:
        """
        Returns total death and daily change per day
        :return: DataFrame. Date/TotalDeath/ChangeInTotal/ChangeInTotal%
        """
        td_data = Gathering.read_avoid_403(url=url)
        return td_data[0]

    @staticmethod
    def get_daily_deaths_data(url: str = URL_DEATH_TOLL) -> pd.DataFrame:
        """
        Returns daily death and change of it compared to day before
        :return: DataFrame. Date/DailyDeath/ChangeInDaily/ChangeInDaily%
        """
        td_data = Gathering.read_avoid_403(url=url)
        return td_data[1]

    @staticmethod
    def get_sex_data(url: str = URL_AGE_SEX_DATA) -> pd.DataFrame:
        """
        Returns death rate by sex(male/female)
        :return: DataFrame. Sex/DeathRate(ConfirmedCases)/DeathRate(AllCases)
        """
        ncov_data_sex = Gathering.read_avoid_403(url=url)
        return ncov_data_sex[1]

    @staticmethod
    def get_age_data(url: str = URL_AGE_SEX_DATA) -> pd.DataFrame:
        """
        Returns death rate by age distribution
        :return: DataFrame. Age/DeathRate(ConfirmedCases)/DeathRate(AllCases)
        """
        ncov_data_age = Gathering.read_avoid_403(url=url)
        return ncov_data_age[0]

    @staticmethod
    def get_total_data(url: str = URL_GENERAL_DATA) -> pd.DataFrame:
        """
        Returns the main table imported from worldometers.
        :return: DataFrame.
        """
        ncov_data_cases = Gathering.read_avoid_403(url=url)
        return ncov_data_cases[0]
