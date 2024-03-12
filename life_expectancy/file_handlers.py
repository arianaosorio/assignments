"""
Module that contains the functions for saving a dataset.
"""

import os
import pandas as pd


def save_data(dataset: pd.DataFrame, file_name: str, data_dir_path: str) -> None:
    """
    Save the data into a file.

    :param dataset: A pandas dataframe with the data to save to a file.
    :param file_name: The name of the file to save.
    :param data_dir_path: The path of data directory.
    """
    dataset.to_csv(os.path.join(data_dir_path, file_name), index=False)
