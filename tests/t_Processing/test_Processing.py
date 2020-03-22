from src.Processing.Processing import Process
from src.Utils.Loader import Loader


TABLE_PATH = "/Users/yigitbaser/Coronavirusmodel/Storage/2020-03-22/TotalTable_77.csv"
#TODO check if pytest return type while using assert
def test_country_names() -> int:
    result = Process.get_country_case_number(country="France",data_type='TotalCases',total_case_table_path=TABLE_PATH)
    assert result == 14459

def test_calculate_total_cases():
    total_case_num_table = Loader.load_data(file_path = TABLE_PATH)
    total_case_num = total_case_num_table[total_case_num_table['Country,Other'] == 'Total:']['TotalCases'].sum()
    tot_cases = Process.calculate_total_cases()

    assert tot_cases/2 == total_case_num

def test_total_deaths():
    pass
