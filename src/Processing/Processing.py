"""
To process data from main table
"""
from src.Utils.Loader import Loader


class Process():
    """
    In order to process data from total table -- DECIDE HOW IT WILL WORK LATER
    """
    table_path = "/Users/yigitbaser/Coronavirusmodel/Storage/2020-03-22/TotalTable_77.csv"

    def __init__(self):
        # version = 'firstVersion'
        self.table_path = "/Users/yigitbaser/Coronavirusmodel/Storage/2020-03-22/TotalTable_77.csv"

    @staticmethod
    def get_country_case_number(country: str, data_type: str, total_case_table_path: str) -> int:
        """
        Returns case number by country
        :param country: str. Country
        :param data_type: str. Which data type from main table
        :param total_case_table_path: str. Table path
        :return: value of data type looking for
        """
        total_case_table = Loader.load_data(total_case_table_path)
        return int(total_case_table[total_case_table['Country,Other'] == country][data_type])

    @staticmethod
    def calculate_total_cases(total_case_table_path: str = table_path) -> int:
        """
        Calculates the number of total cases
        :return: int. Total cases
        """
        total_table = Loader.load_data(total_case_table_path)
        return total_table['TotalCases'].sum()

    # TODO check this fucntion, write tests
    @staticmethod
    def get_active_cases(total_case_table_path: str = table_path):
        """
        Calculates active cases
        :param total_case_table_path:
        :return:
        """
        total_case_table = Loader.load_data(total_case_table_path)
        return total_case_table

    @staticmethod
    def get_total_deaths(total_case_table_path: str = table_path):
        """
        To write
        :param total_case_table_path:
        :return:
        """
