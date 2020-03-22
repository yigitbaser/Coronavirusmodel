from src.Utils.Loader import Loader
import pandas as pd


class Process():
    TABLE_PATH = "/Users/yigitbaser/Coronavirusmodel/Storage/2020-03-22/TotalTable_77.csv"

    def __init__(self):
        version = 'firstVersion'
        self.TABLE_PATH= "/Users/yigitbaser/Coronavirusmodel/Storage/2020-03-22/TotalTable_77.csv"

    def get_country_case_number(country :str, data_type: str, total_case_table_path: str) -> int:
        total_case_table = Loader.load_data(total_case_table_path)
        return int(total_case_table[total_case_table['Country,Other'] == country][data_type])

    def calculate_total_cases(total_case_table_path : str = TABLE_PATH ):
        total_table = Loader.load_data(total_case_table_path)
        return total_table['TotalCases'].sum()

    #TODO check this fucntion, write tests
    def get_active_cases(self, total_case_table_path : str = TABLE_PATH ):
        total_case_table = Loader.load_data(total_case_table_path)
        return total_case_table

    def get_total_deaths(self, total_case_table_path : str = TABLE_PATH ):



