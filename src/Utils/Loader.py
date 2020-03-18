import  pandas as pd


def load_data():
    FILE_NAME = '/Users/yigitbaser/Coronavirusmodel/Storage/2020-03-18/TotalTable_1933.csv'

    df = pd.read_csv(FILE_NAME)
    return df