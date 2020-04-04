"""
Data Exceptions
"""
# TODO FIX ALL FILE
from src.Exceptions import custom_data_exception

class DataImportException(custom_data_exception.CustomException):
    """
    Exception to throw while importing data from website
    """
    def __init__(self) -> None:
        custom_data_exception.__init__(self, "Data Import Exception.")
