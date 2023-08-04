"""
Constants used throughout the project.
"""

import os
from pathlib import Path

CURRENT_DIR = Path(__file__).parent.resolve()
DATA_DIR = os.path.join(CURRENT_DIR, "data")
FILE_PATH = os.path.join(DATA_DIR, "eu_life_expectancy_raw.tsv")
FILE_NAME = "pt_life_expectancy.csv"
