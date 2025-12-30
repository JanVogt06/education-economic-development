"""
Lädt die World Development Indicators (WDI) der Weltbank herunter.
"""

import zipfile
from pathlib import Path
from urllib.request import urlretrieve

import pandas as pd

# Pfade
DATA_DIR = Path(__file__).parent.parent.parent / "data"
RAW_DIR = DATA_DIR / "raw"

# Download-URL
WDI_URL = "https://databank.worldbank.org/data/download/WDI_CSV.zip"


def download_wdi_data(force: bool = False) -> pd.DataFrame:
    """
    Lädt den kompletten WDI-Datensatz herunter.

    Args:
        force: Wenn True, wird auch bei vorhandener Datei neu heruntergeladen.

    Returns:
        DataFrame mit allen WDI-Daten.
    """
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    zip_file = RAW_DIR / "WDI_CSV.zip"
    csv_file = RAW_DIR / "WDICSV.csv"

    # Download falls nötig
    if not zip_file.exists() or force:
        print(f"      Lade {WDI_URL}...")
        urlretrieve(WDI_URL, zip_file)
        print(f"      Gespeichert in {zip_file}")

    # Entpacken falls nötig
    if not csv_file.exists() or force:
        print(f"      Entpacke {zip_file}...")
        with zipfile.ZipFile(zip_file, "r") as z:
            z.extractall(RAW_DIR)

    # CSV laden
    print(f"      Lade {csv_file}...")
    df = pd.read_csv(csv_file)

    return df