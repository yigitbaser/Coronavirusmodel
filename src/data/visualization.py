"""
Stuff to plot the data
"""
import matplotlib.pyplot as plt
import pandas as pd

from src.Utils.Loader import Loader


class Visual():
    """
    Basic first functions for plotting
    """

    def __init__(self, table_path="/Users/yigitbaser/Coronavirusmodel/Storage/"
                                  "2020-03-22/DATATOTALDEATH_77.csv_77.csv",
                 plot_type=None):
        self.plot_type = plot_type
        self.table_path = table_path

    @staticmethod
    def visual(filename: str):
        """
        first try
        :param filename:
        :return:
        """
        plt.figure()
        data_frame = pd.read_csv(filename)
        data_frame.plot(x='Country,Other', y='TotalCases', kind='scatter')
        plt.show()

    @staticmethod
    def plot_total_death(directory: str):
        """
        Plot total death
        :return:
        """
        death_data = Loader.load_data(directory)
        plt.figure()
        death_data.plot(x='Date', y='Total Deaths')
        # df.plot(xdata='Date', ydata='Total Deaths')
        plt.show()
