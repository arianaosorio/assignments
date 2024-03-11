"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.strategies import TSVStrategy
from life_expectancy.enums import Country


def test_clean_data(eu_life_expectancy_raw_fixture, pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    pt_life_expectancy_actual = TSVStrategy().clean_data(
        eu_life_expectancy_raw_fixture, Country.PT.value  # pylint: disable=no-member
    ).reset_index(drop=True)
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
