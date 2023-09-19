"""Tests for the main module"""
from unittest.mock import patch

import pandas as pd

from life_expectancy.main import main

from . import FIXTURES_DIR, OUTPUT_DIR


@patch("life_expectancy.main.save_data")
def test_main(mock, pt_life_expectancy_expected):
    """Run the `main` function and compare the output to the expected output"""
    mock.side_effect = print("Mocking save data")
    eu_life_expectancy_actual = main(
        OUTPUT_DIR, "PT", FIXTURES_DIR / "eu_life_expectancy_raw_fixture.tsv"
    ).reset_index(drop=True)
    pd.testing.assert_frame_equal(
        eu_life_expectancy_actual, pt_life_expectancy_expected
    )
