"""
Module that contains all functions to clean dataset.
"""

import pandas as pd
from life_expectancy.enums import Country
from life_expectancy.file_handlers import TSVFileHandler, JSONFileHandler

from abc import ABC, abstractmethod


class Cleaner(ABC):
    """
    Abstract Class to define cleaner classes.
    """
    @abstractmethod
    def clean_data(self, dataset: pd.DataFrame) -> pd.DataFrame:
        """
        Clean the raw data.
        """


class TSVCleaner(Cleaner):
    """
    Clean the raw data from TSV file.
    """

    def clean_data(self, dataset: pd.DataFrame, country_code: Country) -> pd.DataFrame:
        data = dataset.copy()

        data[["unit", "sex", "age", "region"]] = data["unit,sex,age,geo\\time"].str.split(
            ",", expand=True
        )

        data.drop(columns=["unit,sex,age,geo\\time"], inplace=True)

        data = pd.melt(data, id_vars=["unit", "sex", "age", "region"], var_name="year")

        data["year"] = data["year"].astype("int")
        data["value"] = data.value.str.extract(r"(\d+\.\d)").astype("float")

        clean_dataset = data.dropna()

        dataset_output = clean_dataset[clean_dataset.region == country_code]

        return dataset_output


class JSONCleaner(Cleaner):
    """
    Clean the raw data from JSON file.
    """
    
    def clean_data(self, dataset: pd.DataFrame, country_code: Country) -> pd.DataFrame:
        data = dataset.copy()

        data.rename(columns={'country': 'region', 'life_expectancy': 'value'}, inplace=True)

        data = data[data.region == country_code]

        return data
