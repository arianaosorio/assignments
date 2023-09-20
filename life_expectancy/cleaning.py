"""
Module that contains all functions to clean dataset.
"""

import pandas as pd


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
