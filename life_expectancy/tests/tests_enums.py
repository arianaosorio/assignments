"""
Tests for enums module.
"""

from life_expectancy.enums import Country

def test_country_enum():
    """
    Function that test the actual countries method.
    """
    actual_countries = Country.get_actual_countries()
    expected_countries = [
        "AT",
        "BE",
        "BG",
        "CH",
        "CY",
        "CZ",
        "DK",
        "EE",
        "EL",
        "ES",
        "FI",
        "FR",
        "HR",
        "HU",
        "IS",
        "IT",
        "LI",
        "LT",
        "LU",
        "LV",
        "MT",
        "NL",
        "NO",
        "PL",
        "PT",
        "RO",
        "SE",
        "SI",
        "SK",
        "DE",
        "AL",
        "IE",
        "ME",
        "MK",
        "RS",
        "AM",
        "AZ",
        "GE",
        "TR",
        "UA",
        "BY",
        "UK",
        "XK",
        "FX",
        "MD",
        "SM",
        "RU"
    ]

    assert actual_countries == expected_countries
