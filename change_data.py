import pandas as pd
from rapidfuzz import process, fuzz
from unidecode import unidecode
import requests
from bs4 import BeautifulSoup

# ================================================
# CONFIGURATION
# ================================================
CSV_PATH = 'data.csv'
SIMILARITY_THRESHOLD = 80  # percent for fuzzy matching

# List of all expected columns in the CSV
COLUMNS = [
    'Name', 'Age', 'Gender', 'Sport', 'Discipline', 'Height (cm)', 'Weight (kg)', 'BMI',
    'Leg Length (cm)', 'Torso Length (cm)', 'Chest Circumference (cm)', 'Waist Circumference (cm)',
    'Hip Circumference (cm)', 'Arm Length (cm)', 'Wingspan (cm)', 'Thigh Circumference (cm)',
    'Calf Circumference (cm)', 'Bicep Circumference (cm)', 'Wrist Circumference (cm)',
    'Body Fat Percentage (%)', 'Muscle Mass (kg)', 'Morphotype', 'Career Start Year', 'Career End Year'
]

# ================================================
# UTILITY FUNCTIONS
# ================================================

def normalize_name(name: str) -> str:
    """Lowercase, strip accents, and remove extra whitespace."""
    return unidecode(name).lower().strip()


def find_similar(name: str, choices: list, threshold: int = SIMILARITY_THRESHOLD) -> list:
    """
    Return a list of (match, score) from choices whose fuzzy match score >= threshold.
    """
    matches = process.extract(name, choices, scorer=fuzz.token_sort_ratio, limit=5)
    return [(m, score) for m, score, _ in matches if score >= threshold]


