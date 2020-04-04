"""
Exception
"""


class CustomException(Exception):
    """
    Parent class template for custom data exceptions
    """

    def __init__(self, exc_name: str) -> None:
        """
        Sets up the parameters.
        :param exc_name: str. Name of exception.
        """
        Exception.__init__(self)

        self.exc_name = exc_name
        self.code: int = 0  # Code of the exception.
        self.description: str = ""  # Description of the exception.

    def __str__(self) -> str:
        """
        Overrides the print method.
        :return: str. The description of the exception
        """
        return str(self.code) + " " + self.exc_name + " " + self.description
