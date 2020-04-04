import pandas as pd
from ABC import Any

class Loader():

    def load_data(file_path :str,index_col_pass: Any=None):
        df = pd.read_csv(file_path,index_col=index_col_pass)
        return df