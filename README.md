# Bildung und wirtschaftliche Entwicklung

Eine Analyse des Zusammenhangs zwischen Bildungsindikatoren und wirtschaftlicher Entwicklung anhand der World Development Indicators der Weltbank.

## Forschungsfragen

1. **RQ1:** Gibt es einen Zusammenhang zwischen Bildung und wirtschaftlicher Entwicklung?
2. **RQ2:** Welche Faktoren beeinflussen das BIP pro Kopf am stärksten?
3. **RQ3:** Wie hat sich der Zusammenhang zwischen Bildung und BIP über die Jahrzehnte entwickelt?

## Hypothesen

- **H1:** Positive Korrelation zwischen Sekundarschuleinschreibung und BIP pro Kopf *(RQ1)*
- **H2:** Positive Korrelation zwischen Bildungsausgaben (% BIP) und BIP pro Kopf *(RQ1)*
- **H3:** Die Korrelation Bildung-BIP ist in den 2010ern stärker als in den 1990ern *(RQ3)*
- **H4:** Tertiärbildung korreliert stärker mit BIP als Primärbildung *(RQ2)*

## Datenquelle

[World Development Indicators (WDI)](https://datatopics.worldbank.org/world-development-indicators/) der Weltbank – über 1.400 Indikatoren zu Wirtschaft, Bildung, Gesundheit für 200+ Länder seit 50 Jahren.

## Projektstruktur

```
├── data/
│   ├── raw/            # Rohdaten (WDI)
│   ├── interim/        # Zwischenergebnisse
│   └── processed/      # Finale Datensätze
├── models/             # Trainierte Modelle
├── notebooks/          # Jupyter Notebooks
├── src/                # Python-Module
└── README.md
```

## Setup

```bash
pip install -r requirements.txt
python src/main.py
```

## Methodik

1. **Explorative Datenanalyse:** Überblick über verfügbare Indikatoren, Datenqualität, fehlende Werte
2. **Statistische Tests:** Korrelationsanalysen, Signifikanztests für die Hypothesen
3. **Machine Learning:** Random Forest zur BIP-Vorhersage mit Feature Importance Analyse
4. **Visualisierung:** Darstellung der Ergebnisse

---

## Wie funktioniert das Projekt?

Das Projekt besteht aus vier Jupyter Notebooks, die aufeinander aufbauen. Die Notebooks dokumentieren die Analyse und begründen alle Entscheidungen. Der wiederverwendbare Code liegt in `src/` und wird über `main.py` ausgeführt.

### Notebook 1: Explorative Datenanalyse (`01_eda.ipynb`)

Hier lernen wir den Datensatz kennen: Wie sind die Daten strukturiert? Welche Indikatoren gibt es? Wie viele fehlende Werte haben wir? Welcher Zeitraum ist gut abgedeckt?

Am Ende wissen wir, was wir in der Datenaufbereitung tun müssen.

### Notebook 2: Datenaufbereitung (`02_data_preparation.ipynb`)

Hier dokumentieren wir die Entscheidungen für die Datentransformation: Welche Länder und Indikatoren behalten wir? Welchen Zeitraum? Welches Format brauchen wir für die Analyse?

Die Entscheidungen werden begründet, der eigentliche Code landet in `src/features/build_features.py`. Output sind zwei CSV-Dateien in `data/processed/`.

### Notebook 3: Hypothesentests (`03_hypothesis_testing.ipynb`)

Hier testen wir die vier Hypothesen mit statistischen Tests (Pearson/Spearman-Korrelation, Fisher's z-Transformation). Jeder Test wird durchgeführt, visualisiert und interpretiert.

Die Ergebnisse beantworten direkt unsere drei Forschungsfragen.

### Notebook 4: Machine Learning (`04_modeling.ipynb`)

Hier dokumentieren wir die Entscheidungen für das Vorhersagemodell: Warum Random Forest? Welche Features? Wie gehen wir mit fehlenden Werten um?

Der Code liegt in `src/features/train_model.py`. Output ist ein trainiertes Modell in `models/` sowie eine Feature Importance Analyse.

---

## Ergebnisse

| Hypothese | Ergebnis | Signifikant? |
|-----------|----------|--------------|
| H1: Sekundarbildung ↔ BIP | ρ = 0.80 | ✓ Ja |
| H2: Bildungsausgaben ↔ BIP | ρ = 0.26 | ✓ Ja (schwach) |
| H3: 1990er → 2010er | 0.71 → 0.76 | ✓ Ja |
| H4: Tertiär vs. Primär | 0.77 vs. 0.06 | ✓ Ja |

**Feature Importance (Random Forest):**
1. Sekundarbildung (43%)
2. Tertiärbildung (21%)
3. Bildungsausgaben (20%)
4. Primärbildung (16%)

---

## Autor

Jan Vogt – Universität Jena, 3. Semester