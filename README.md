# Bildung und wirtschaftliche Entwicklung

Eine Analyse des Zusammenhangs zwischen Bildungsindikatoren und wirtschaftlicher Entwicklung anhand der World Development Indicators der Weltbank.

## Forschungsfragen

1. **RQ1:** Gibt es einen Zusammenhang zwischen Bildung und wirtschaftlicher Entwicklung?
2. **RQ2:** Welche Faktoren beeinflussen das BIP pro Kopf eines Landes am stärksten?
3. **RQ3:** Wie hat sich der Zusammenhang zwischen Bildung und BIP über die Jahrzehnte verändert?

## Hypothesen

- **H1:** Die Einschulungsrate in der Sekundarstufe korreliert signifikant positiv mit dem BIP pro Kopf. *(RQ1)*
- **H2:** Länder mit höheren Bildungsausgaben (% des BIP) haben ein signifikant höheres BIP pro Kopf. *(RQ1)*
- **H3:** Die Einschulungsrate hat einen stärkeren Zusammenhang mit dem BIP pro Kopf als die Bildungsausgaben. *(RQ2)*
- **H4:** Der Zusammenhang zwischen Bildung und BIP ist in den letzten 30 Jahren stärker geworden. *(RQ3)*

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
3. **Machine Learning:** Vorhersagemodell für BIP pro Kopf (geplant)
4. **Visualisierung:** Darstellung der Ergebnisse

---

## Wie funktioniert das Projekt?

Das Projekt besteht aus drei Jupyter Notebooks, die aufeinander aufbauen. Die Notebooks dokumentieren die Analyse und begründen alle Entscheidungen. Der wiederverwendbare Code liegt in `src/` und wird über `main.py` ausgeführt.

### Notebook 1: Explorative Datenanalyse (`01_eda.ipynb`)

Hier lernen wir den Datensatz kennen: Wie sind die Daten strukturiert? Welche Indikatoren gibt es? Wie viele fehlende Werte haben wir? Welcher Zeitraum ist gut abgedeckt?

Am Ende wissen wir, was wir in der Datenaufbereitung tun müssen.

### Notebook 2: Datenaufbereitung (`02_data_preparation.ipynb`)

Hier dokumentieren wir die Entscheidungen für die Datentransformation: Welche Länder und Indikatoren behalten wir? Welchen Zeitraum? Welches Format brauchen wir für die Analyse?

Die Entscheidungen werden begründet, der eigentliche Code landet in `src/features/build_features.py`. Output sind zwei CSV-Dateien in `data/processed/`.

### Notebook 3: Hypothesentests (`03_hypothesis_testing.ipynb`)

Hier testen wir die vier Hypothesen mit statistischen Tests (Pearson/Spearman-Korrelation, Fisher's z-Transformation, Steiger's Z-Test). Jeder Test wird durchgeführt, visualisiert und interpretiert.

Die Ergebnisse beantworten direkt unsere drei Forschungsfragen.

---

## Autor

Jan Vogt – Universität Jena, 3. Semester