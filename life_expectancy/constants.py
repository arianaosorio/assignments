"""
Constants used throughout the project.
"""

import os
from pathlib import Path

CURRENT_DIR = Path(__file__).parent.resolve()
DATA_DIR = os.path.join(CURRENT_DIR, "data")
