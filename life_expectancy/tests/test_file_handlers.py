"""
Tests for the file handlers module.
"""

import os
from unittest import mock

import pandas as pd

from life_expectancy.file_handlers import load_data, save_data

from . import FIXTURES_DIR


def test_load_data():
    """
    Run unit test of function `load_data`.
    """
    actual_data = load_data(FIXTURES_DIR / "dummy_dataset.tsv")
    expected_data = pd.DataFrame.from_dict(
        {
            "col_1,col_2,col_3": ["1,5,23", "1,5,39", "x1,x2,x3"],
            "2021": [79, 61, 70],
            "2020": [85, 60, 50],
        }
    )

    pd.testing.assert_frame_equal(actual_data, expected_data)


def test_save_data():
    """
    Run unit test of function `save_data`.
    """
    test_df = pd.DataFrame.from_dict({"col_1": [1, 2, 3], "col_2": [1, 5, 6]})
    with mock.patch("pandas.DataFrame.to_csv") as to_csv_mock:
        to_csv_mock.side_effect = print("Mocking saving data")
        save_data(test_df, "output_test.csv", FIXTURES_DIR)
        to_csv_mock.assert_called_with(
            os.path.join(FIXTURES_DIR, "output_test.csv"), index=False
        )
