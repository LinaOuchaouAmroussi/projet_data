# -*- coding: utf-8 -*-
"""
Module de nettoyage des données brutes.

Ce module lit les données brutes CSV depuis data/raw/, effectue les opérations
de nettoyage (valeurs manquantes, doublons, normalisation des colonnes)
et sauvegarde le résultat dans data/cleaned/.
"""

import os
import sys
import pandas as pd

# === S'assurer que le répertoire projet_data est dans le path ===
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from config import RAW_DIR, CLEAN_DIR, DATA_RAW_PATH, DATA_CLEAN_PATH


def clean_data():
    """Nettoie les données CSV et les enregistre dans data/cleaned/."""
    os.makedirs(CLEAN_DIR, exist_ok=True)

    print("Lecture du fichier brut...")
    df = pd.read_csv(DATA_RAW_PATH, low_memory=False)

    print("Nettoyage des données...")

    numeric_columns = [
        "Note Ecart rémunération",
        "Note Ecart taux d'augmentation (hors promotion)",
        "Note Ecart taux de promotion",
        "Note Ecart taux d'augmentation",
        "Note Retour congé maternité",
        "Note Hautes rémunérations",
        "Note Index",
    ]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.drop_duplicates()
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    print("Sauvegarde du fichier nettoyé...")
    df.to_csv(DATA_CLEAN_PATH, index=False)
    print(f"Données nettoyées enregistrées dans : {DATA_CLEAN_PATH}")


if __name__ == "__main__":
    clean_data()

# ------------------------------------------------------------
# Fin de clean_data.py
# ------------------------------------------------------------
