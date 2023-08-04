"""
Module that contains the main function to run the process.
"""

import argparse

import pandas as pd

from life_expectancy.cleaning import clean_data
from life_expectancy.constants import DATA_DIR, FILE_NAME, FILE_PATH
from life_expectancy.file_handlers import load_data, save_data


def main(
    file_path: str, file_name: str, data_dir_path: str, country: str = "PT"
) -> pd.DataFrame:
    """
    Loads and clean raw dataset. Saves the cleaned dataset.

    :param file_path: The file path.
    :param file_name: The name of the file to save.
    :param data_dir_path: The path of data directory.
    :param country: The name of country.
    :returns: A pandas dataframe with the cleaned data.
    """
    dataset = load_data(file_path)
    clean_dataset = clean_data(dataset, country)
    save_data(clean_dataset, file_name, data_dir_path)

    return clean_dataset


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description="Clean and save life expectancy data")
    parser.add_argument(
        "--country", type="str", default="PT", help="The country code to clean data for"
    )
    args = parser.parse_args()
    main(FILE_PATH, FILE_NAME, DATA_DIR, args.country)
