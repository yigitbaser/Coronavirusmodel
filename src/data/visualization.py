import matplotlib.pyplot as plt
import pandas as pd
from src.Utils.Loader import Loader


class visual():
    def __init__(self, table_path ="/Users/yigitbaser/Coronavirusmodel/Storage/2020-03-22/DATATOTALDEATH_77.csv_77.csv",plot_type=None):
        self.plot_type= plot_type
        self.table_path =table_path

    def visual(self,filename :str):
        plt.figure()
        df = pd.read_csv(filename)
        df.plot(x='Country,Other',y='TotalCases',kind='scatter')
        plt.show()

    def plot_total_death():
        """

        :return:
        """
        death_data = Loader.load_data("/Users/yigitbaser/Coronavirusmodel/Storage/2020-03-22/DATATOTALDEATH_77.csv")
        plt.figure()
        death_data.plot(x='Date', y='Total Deaths')
        #df.plot(xdata='Date', ydata='Total Deaths')
        plt.show()