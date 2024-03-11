"""
Context module pipeline - Strategy Pattern
"""

from abc import ABC, abstractmethod

import pandas as pd

from life_expectancy.enums import Country
from life_expectancy.file_handlers import TSVFileHandler, JSONFileHandler
from life_expectancy.cleaning import TSVCleaner, JSONCleaner


class Strategy(ABC):
    """
    Abstract class to define strategies classes.
    """
    @abstractmethod
    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Abstract `load_data` class method of Strategy class.
        """

    @abstractmethod
    def clean_data(self, dataset: pd.DataFrame, country: Country) -> pd.DataFrame:
        """
        Abstract `clean_data` class method of Strategy class.
        """

class TSVStrategy(Strategy):
    """
    Strategy class for TSV files.
    """
    def load_data(self, file_path: str) -> pd.DataFrame:
        dataset = TSVFileHandler().load_data(file_path)
        return dataset

    def clean_data(self, dataset: pd.DataFrame, country: Country) -> pd.DataFrame:
        clean_dataset = TSVCleaner().clean_data(dataset, country)
        return clean_dataset


class JSONStrategy(Strategy):
    """
    Strategy class for JSON files.
    """
    def load_data(self, file_path: str) -> pd.DataFrame:
        dataset = JSONFileHandler().load_data(file_path)
        return dataset

    def clean_data(self, dataset: pd.DataFrame, country: Country) -> pd.DataFrame:
        clean_dataset = JSONCleaner().clean_data(dataset, country)
        return clean_dataset
