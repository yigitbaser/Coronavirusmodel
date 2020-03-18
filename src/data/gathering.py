"""
Gathers data from www.worldometers.info

"""
import pandas as pd

URL_GENERAL_DATA = 'https://www.worldometers.info/coronavirus'
URL_AGE_SEX_DATA = 'https://www.worldometers.info/coronavirus/coronavirus-age-sex-demographics/'
URL_DEATH_TOLL = 'https://www.worldometers.info/coronavirus/coronavirus-death-toll/'

class gathering:
    """
    Includes functions to get data from website
    """
    def get_total_data() -> pd.DataFrame:
        """
        Returns the main table imported from worldometers.
        :return: DataFrame.
        """
        ncov_data_cases = pd.read_html(URL_GENERAL_DATA)
        ncov_data_df = ncov_data_cases[0]
        return ncov_data_df

    def get_age_data() -> pd.DataFrame:
        """
        Returns death rate by age distribution
        :return: DataFrame. Age/DeathRate(ConfirmedCases)/DeathRate(AllCases)
        """
        ncov_data_age = pd.read_html(URL_AGE_SEX_DATA)
        ncov_data_age_df = ncov_data_age[0]
        return ncov_data_age_df

    def get_sex_data() -> pd.DataFrame:
        """
        Returns death rate by sex(male/female)
        :return: DataFrame. Sex/DeathRate(ConfirmedCases)/DeathRate(AllCases)
        """
        ncov_data_sex = pd.read_html(URL_AGE_SEX_DATA)
        ncov_data_sex_df = ncov_data_sex[1]
        return ncov_data_sex_df

    def get_precondition_data() -> pd.DataFrame:
        """
        Returns death rate by precondition(male/female)
        :return: DataFrame. PreexistingCondition/DeathRate(ConfirmedCases)/DeathRate(AllCases)
        """

        ncov_data_precon = pd.read_html(URL_AGE_SEX_DATA)
        ncov_data_precon_df = ncov_data_precon[2]
        return ncov_data_precon_df

    def get_total_deaths_data() -> pd.DataFrame:
        """
        Returns total death and daily change per day
        :return: DataFrame. Date/TotalDeath/ChangeInTotal/ChangeInTotal%
        """
        td_data = pd.read_html(URL_DEATH_TOLL)
        return td_data[0]

    def get_daily_deaths_data() -> pd.DataFrame:
        """
        Returns daily death and change of it compared to day before
        :return: DataFrame. Date/DailyDeath/ChangeInDaily/ChangeInDaily%
        """
        td_data = pd.read_html(URL_DEATH_TOLL)
        return td_data[1]