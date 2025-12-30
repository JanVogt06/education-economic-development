#!/usr/bin/env python3
"""
Hauptskript für das Data Science Projekt.
Führt die komplette Pipeline aus: Daten laden, verarbeiten, analysieren.
"""

from data.make_dataset import download_wdi_data
from features.build_features import build_features


def main():
    """Führt die komplette Analyse-Pipeline aus."""
    print("=" * 60)
    print("Bildung und wirtschaftliche Entwicklung - Analyse")
    print("=" * 60)

    # 1. Daten laden
    print("\n[1/4] Lade World Development Indicators...")
    df = download_wdi_data()
    print(f"      Datensatz geladen: {df.shape[0]:,} Zeilen, {df.shape[1]:,} Spalten")

    # 2. Features erstellen
    print("\n[2/4] Feature Engineering...")
    df_long, df_pivot = build_features()

    # 3. Modell trainieren (TODO)
    print("\n[3/4] Modell Training...")
    print("      (noch nicht implementiert)")

    # 4. Evaluation (TODO)
    print("\n[4/4] Evaluation...")
    print("      (noch nicht implementiert)")

    print("\n" + "=" * 60)
    print("Pipeline abgeschlossen.")
    print("=" * 60)


if __name__ == "__main__":
    main()