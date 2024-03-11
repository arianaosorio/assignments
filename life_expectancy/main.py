"""
Module that contains the main function to run the process.
"""

import argparse
import os

import pandas as pd

from life_expectancy.strategies import TSVStrategy, JSONStrategy
from life_expectancy.constants import DATA_DIR
from life_expectancy.file_handlers import save_data


def main(
    data_dir_path: str,
    country: str = "PT",
    file_path: str = os.path.join(DATA_DIR, "eu_life_expectancy_raw.tsv"),
    extension_file: str = ".tsv"
) -> pd.DataFrame:
    """
    Loads and clean raw dataset. Saves the cleaned dataset.

    :param file_path: The file path to load.
    :param data_dir_path: The path of data directory.
    :param country: The name of country.
    :returns: A pandas dataframe with the cleaned data.
    """
    strategies_dict = {
        '.tsv': TSVStrategy(),
        '.json': JSONStrategy()
    }

    strategy = strategies_dict[extension_file]

    dataset = strategy.load_data(file_path)
    clean_dataset = strategy.clean_data(dataset, country)
    save_data(clean_dataset, f"{country.lower()}_life_expectancy.csv", data_dir_path)

    return clean_dataset


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description="Clean and save life expectancy data")
    parser.add_argument(
        "--country", type=str, default="PT", help="The country code to clean data for"
    )
    parser.add_argument(
        "--file_path",
        type=str,
        default=os.path.join(DATA_DIR, "eu_life_expectancy_raw.tsv"),
        help="Specify data file path",
    )
    parser.add_argument(
        "--extension_file",
        type=str,
        default=".tsv",
        help="Specify the type of extension file"
    )
    args = parser.parse_args()
    main(DATA_DIR, **vars(args))
