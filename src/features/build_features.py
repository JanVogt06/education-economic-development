"""
Datenaufbereitung für das Bildung-Wirtschaft-Projekt.

Transformiert die Rohdaten in analysefertige Datensätze.
Entscheidungen basieren auf der Exploration in notebooks/02_data_preparation.ipynb
"""

from pathlib import Path

import pandas as pd

# Pfade
DATA_DIR = Path(__file__).parent.parent.parent / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

# Konfiguration (aus Notebook-Exploration)
START_YEAR = 1990
END_YEAR = 2023

INDICATORS = {
    # BIP
    "NY.GDP.PCAP.CD": "GDP per capita (current US$)",
    "NY.GDP.PCAP.PP.CD": "GDP per capita, PPP (current international $)",

    # Bildung - Einschulungsraten
    "SE.SEC.ENRR": "School enrollment, secondary (% gross)",
    "SE.SEC.NENR": "School enrollment, secondary (% net)",
    "SE.PRM.ENRR": "School enrollment, primary (% gross)",
    "SE.TER.ENRR": "School enrollment, tertiary (% gross)",

    # Bildung - Ausgaben
    "SE.XPD.TOTL.GD.ZS": "Government expenditure on education, total (% of GDP)",
    "SE.XPD.TOTL.GB.ZS": "Government expenditure on education, total (% of government expenditure)",
}


def build_features() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Baut die Features aus den Rohdaten.

    Returns:
        Tuple aus (df_long, df_pivot)
    """
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Rohdaten laden
    print("      Lade Rohdaten...")
    df = pd.read_csv(RAW_DIR / "WDICSV.csv")
    countries = pd.read_csv(RAW_DIR / "WDICountry.csv")

    # 2. Nur echte Länder (keine Aggregate)
    print("      Filtere echte Länder...")
    real_countries = countries[countries["Region"].notna()]["Country Code"].tolist()
    df = df[df["Country Code"].isin(real_countries)]

    # 3. Nur relevante Indikatoren
    print("      Filtere Indikatoren...")
    df = df[df["Indicator Code"].isin(INDICATORS.keys())]

    # 4. Ins Long-Format transformieren
    print("      Transformiere ins Long-Format...")
    year_cols = [col for col in df.columns if col.isdigit()]

    df_long = df.melt(
        id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],
        value_vars=year_cols,
        var_name="Year",
        value_name="Value"
    )

    # Year als Integer
    df_long["Year"] = pd.to_numeric(df_long["Year"], errors="coerce")

    # Zeitraum filtern
    df_long = df_long[(df_long["Year"] >= START_YEAR) & (df_long["Year"] <= END_YEAR)]

    # NaN-Werte entfernen
    df_long = df_long.dropna(subset=["Value"])

    # 5. Pivot-Format für Korrelationsanalysen
    print("      Erstelle Pivot-Format...")
    df_pivot = df_long.pivot_table(
        index=["Country Name", "Country Code", "Year"],
        columns="Indicator Code",
        values="Value"
    ).reset_index()

    # Spaltenname-Index entfernen (von pivot_table)
    df_pivot.columns.name = None

    # 6. Speichern
    print("      Speichere Ergebnisse...")
    df_long.to_csv(PROCESSED_DIR / "wdi_long.csv", index=False)
    df_pivot.to_csv(PROCESSED_DIR / "wdi_pivot.csv", index=False)

    print(f"      Long-Format: {len(df_long):,} Zeilen")
    print(f"      Pivot-Format: {len(df_pivot):,} Zeilen")

    return df_long, df_pivot