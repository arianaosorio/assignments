"""
Module that contains the functions for loading and saving a dataset.
"""

import os
from abc import ABC, abstractmethod
import pandas as pd


class FileHandler(ABC):
    """
    Abstract Class to define file handlers classes.
    """
    @abstractmethod
    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Load the raw data from a file.

        :param file_path: The file path.
        :returns: A pandas dataframe with the raw data.
        """


class TSVFileHandler(FileHandler):
    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Load the raw data from tsv file.

        :param file_path: The file path.
        :returns: A pandas dataframe with the raw data.
        """
        return pd.read_csv(file_path, sep="\t")


class JSONFileHandler(FileHandler):
    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Load the raw data from json file.

        :param file_path: The file path.
        :returns: A pandas dataframe with the raw data.
        """
        return pd.read_json(file_path)


def save_data(dataset: pd.DataFrame, file_name: str, data_dir_path: str) -> None:
    """
    Save the data into a file.

    :param dataset: A pandas dataframe with the data to save to a file.
    :param file_name: The name of the file to save.
    :param data_dir_path: The path of data directory.
    """
    dataset.to_csv(os.path.join(data_dir_path, file_name), index=False)
