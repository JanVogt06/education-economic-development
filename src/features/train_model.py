"""
Machine Learning Modell für BIP-Vorhersage.

Trainiert einen Random Forest Regressor, um das BIP pro Kopf
aus Bildungsindikatoren vorherzusagen.
Entscheidungen basieren auf notebooks/04_modeling.ipynb
"""

from pathlib import Path

import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline

# Pfade
DATA_DIR = Path(__file__).parent.parent.parent / "data"
PROCESSED_DIR = DATA_DIR / "processed"
MODELS_DIR = Path(__file__).parent.parent.parent / "models"

# Konfiguration
FEATURE_COLS = [
    "SE.PRM.ENRR",       # Primärschuleinschreibung
    "SE.SEC.ENRR",       # Sekundarschuleinschreibung
    "SE.TER.ENRR",       # Tertiärbildung
    "SE.XPD.TOTL.GD.ZS", # Bildungsausgaben (% BIP)
]

TARGET_COL = "NY.GDP.PCAP.PP.CD"  # BIP pro Kopf (PPP)

FEATURE_NAMES = [
    "Primärbildung",
    "Sekundarbildung",
    "Tertiärbildung",
    "Bildungsausgaben",
]

RANDOM_STATE = 42
TEST_SIZE = 0.2


def train_model() -> dict:
    """
    Trainiert das Random Forest Modell.
    
    Returns:
        Dictionary mit Ergebnissen (Scores, Feature Importance)
    """
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Daten laden
    print("      Lade aufbereitete Daten...")
    df = pd.read_csv(PROCESSED_DIR / "wdi_pivot.csv")
    
    # 2. Features und Target vorbereiten
    print("      Bereite Features vor...")
    df_ml = df.dropna(subset=[TARGET_COL])
    
    X = df_ml[FEATURE_COLS].values
    y = df_ml[TARGET_COL].values
    
    print(f"      Datenpunkte: {len(y):,}")
    
    # 3. Train/Test Split
    print("      Train/Test Split...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )
    
    print(f"      Training: {len(y_train):,}, Test: {len(y_test):,}")
    
    # 4. Random Forest trainieren
    print("      Trainiere Random Forest...")
    rf_model = make_pipeline(
        SimpleImputer(strategy="mean"),
        RandomForestRegressor(n_estimators=100, random_state=RANDOM_STATE)
    )
    rf_model.fit(X_train, y_train)
    
    rf_train_score = rf_model.score(X_train, y_train)
    rf_test_score = rf_model.score(X_test, y_test)
    
    # 5. Lineare Regression zum Vergleich
    print("      Trainiere Lineare Regression (Vergleich)...")
    lr_model = make_pipeline(
        SimpleImputer(strategy="mean"),
        LinearRegression()
    )
    lr_model.fit(X_train, y_train)
    
    lr_train_score = lr_model.score(X_train, y_train)
    lr_test_score = lr_model.score(X_test, y_test)
    
    # 6. Feature Importance
    rf = rf_model.named_steps["randomforestregressor"]
    importances = rf.feature_importances_
    
    importance_df = pd.DataFrame({
        "Feature": FEATURE_NAMES,
        "Importance": importances
    }).sort_values("Importance", ascending=False)
    
    # 7. Modell speichern
    print("      Speichere Modell...")
    joblib.dump(rf_model, MODELS_DIR / "random_forest.joblib")
    importance_df.to_csv(MODELS_DIR / "feature_importance.csv", index=False)
    
    # 8. Ergebnisse zusammenfassen
    results = {
        "rf_train_r2": rf_train_score,
        "rf_test_r2": rf_test_score,
        "lr_train_r2": lr_train_score,
        "lr_test_r2": lr_test_score,
        "feature_importance": importance_df,
        "n_train": len(y_train),
        "n_test": len(y_test),
    }
    
    # Ergebnisse ausgeben
    print(f"\n      Ergebnisse:")
    print(f"      Random Forest  - Train R²: {rf_train_score:.4f}, Test R²: {rf_test_score:.4f}")
    print(f"      Lin. Regression - Train R²: {lr_train_score:.4f}, Test R²: {lr_test_score:.4f}")
    print(f"\n      Feature Importance:")
    for _, row in importance_df.iterrows():
        print(f"        {row['Feature']:20s}: {row['Importance']:.4f}")
    
    return results
