"""
Module that contains all functions to clean dataset.
"""

import argparse
import os
from pathlib import Path

import pandas as pd

CURRENT_DIR = Path(__file__).parent.resolve()
DATA_DIR = os.path.join(CURRENT_DIR, "data")
FILE_PATH = os.path.join(DATA_DIR, "eu_life_expectancy_raw.tsv")
FILE_NAME = "pt_life_expectancy.csv"


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load the raw data from tsv file.

    :param file_path: The file path.
    :returns: A pandas dataframe with the raw data.
    """
    dataset = pd.read_csv(file_path, sep="\t")

    return dataset


def save_data(dataset: pd.DataFrame, file_name: str, data_dir_path: str) -> None:
    """
    Save the data into a file.

    :param dataset: A pandas dataframe with the data to save to a file.
    :param file_name: The name of the file to save.
    :param data_dir_path: The path of data directory.
    """
    dataset.to_csv(os.path.join(data_dir_path, file_name), index=False)


def clean_data(dataset: pd.DataFrame, country: str = "PT") -> pd.DataFrame:
    """
    Clean the raw data.

    :param dataset: A pandas dataframe with the data to clean.
    :param country: The name of country.
    :returns: A pandas dataframe with the cleaned data.
    """
    data = dataset.copy()

    data[["unit", "sex", "age", "region"]] = data["unit,sex,age,geo\\time"].str.split(
        ",", expand=True
    )

    data.drop(columns=["unit,sex,age,geo\\time"], inplace=True)

    data = pd.melt(data, id_vars=["unit", "sex", "age", "region"], var_name="year")

    data["year"] = data["year"].astype("int")
    data["value"] = data.value.str.extract(r"(\d+\.\d)").astype("float")

    clean_dataset = data.dropna()

    dataset_output = clean_dataset[clean_dataset.region == country]

    return dataset_output


def main(
    file_path: str, file_name: str, data_dir_path: str, country: str = "PT"
) -> None:
    """
    Loads and clean raw dataset. Saves the cleaned dataset.

    :param file_path: The file path.
    :param file_name: The name of the file to save.
    :param data_dir_path: The path of data directory.
    :param country: The name of country.
    """
    dataset = load_data(file_path)
    clean_dataset = clean_data(dataset, country)
    save_data(clean_dataset, file_name, data_dir_path)


if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser(description="Clean and save life expectancy data")
    parser.add_argument(
        "--country", type="str", default="PT", help="The country code to clean data for"
    )
    args = parser.parse_args()
    main(FILE_PATH, FILE_NAME, DATA_DIR, args.country)
