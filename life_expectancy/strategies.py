"""
Context module pipeline - Strategy Pattern
"""

from abc import ABC, abstractmethod

import pandas as pd

from life_expectancy.enums import Country


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
    def clean_data(self, dataset: pd.DataFrame, country_code: Country) -> pd.DataFrame:
        """
        Abstract `clean_data` class method of Strategy class.
        """

class TSVStrategy(Strategy):
    """
    Strategy class for TSV files.
    """
    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Load the raw data from tsv file.

        :param file_path: The file path.
        :returns: A pandas dataframe with the raw data.
        """
        return pd.read_csv(file_path, sep="\t")

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


class JSONStrategy(Strategy):
    """
    Strategy class for JSON files.
    """
    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Load the raw data from json file.

        :param file_path: The file path.
        :returns: A pandas dataframe with the raw data.
        """
        return pd.read_json(file_path)

    def clean_data(self, dataset: pd.DataFrame, country_code: Country) -> pd.DataFrame:
        data = dataset.copy()

        data.rename(columns={'country': 'region', 'life_expectancy': 'value'}, inplace=True)

        data = data[data.region == country_code]
