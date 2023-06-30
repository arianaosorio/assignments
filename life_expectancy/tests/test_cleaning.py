"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.cleaning import DATA_DIR, FILE_NAME, FILE_PATH, main

from . import OUTPUT_DIR


def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    main(FILE_PATH, FILE_NAME, DATA_DIR)
    pt_life_expectancy_actual = pd.read_csv(OUTPUT_DIR / "pt_life_expectancy.csv")
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
