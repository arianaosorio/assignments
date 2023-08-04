"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.main import FILE_NAME, main

from . import FIXTURES_DIR, OUTPUT_DIR


def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    eu_life_expectancy_actual = main(
        FIXTURES_DIR / "eu_life_expectancy_raw_fixture.tsv", FILE_NAME, OUTPUT_DIR
    ).reset_index(drop=True)
    pd.testing.assert_frame_equal(
        eu_life_expectancy_actual, pt_life_expectancy_expected
    )
