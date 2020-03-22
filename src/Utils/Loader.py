import pandas as pd

class Loader():

    def load_data(file_path :str ):
        df = pd.read_csv(file_path)
        return df