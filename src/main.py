#!/usr/bin/env python3
"""
Hauptskript für das Data Science Projekt.
Führt die komplette Pipeline aus: Daten laden, verarbeiten, Modell trainieren.
"""

from data.make_dataset import download_wdi_data
from features.build_features import build_features
from features.train_model import train_model


def main():
    """Führt die komplette Analyse-Pipeline aus."""
    print("=" * 60)
    print("Bildung und wirtschaftliche Entwicklung - Analyse")
    print("=" * 60)

    # 1. Daten laden
    print("\n[1/3] Lade World Development Indicators...")
    df = download_wdi_data()
    print(f"      Datensatz geladen: {df.shape[0]:,} Zeilen, {df.shape[1]:,} Spalten")

    # 2. Features erstellen
    print("\n[2/3] Feature Engineering...")
    df_long, df_pivot = build_features()

    # 3. Modell trainieren
    print("\n[3/3] Modell Training...")
    results = train_model()

    print("\n" + "=" * 60)
    print("Pipeline abgeschlossen.")
    print("=" * 60)
    print(f"\nDateien erstellt:")
    print(f"  - data/processed/wdi_long.csv")
    print(f"  - data/processed/wdi_pivot.csv")
    print(f"  - models/random_forest.joblib")
    print(f"  - models/feature_importance.csv")


if __name__ == "__main__":
    main()