"""
Module de nettoyage des données brutes.
Lit la table RAW depuis SQLite, nettoie, harmonise les colonnes
et renvoie un DataFrame propre (le main écrira la table CLEAN).
"""

import pandas as pd
import numpy as np
from config import engine, RAW_TABLE
import re

def _norm(c: str) -> str:
    return (
        c.strip().lower()
         .replace(" ", "_")
         .replace("’", "'")
         .replace("é", "e")
         .replace("è", "e")
         .replace("ê", "e")
         .replace("à", "a")
    )

def _clean_numeric(val):
    """Garde uniquement les chiffres et le point décimal, sinon NaN"""
    if pd.isna(val):
        return np.nan
    # on extrait le premier nombre flottant trouvé dans la chaîne
    match = re.search(r"\d+(\.\d+)?", str(val))
    if match:
        return float(match.group())
    return np.nan

def clean_data() -> pd.DataFrame:
    df = pd.read_sql(f"SELECT * FROM {RAW_TABLE}", con=engine)
    df.columns = [_norm(c) for c in df.columns]

    # on nettoie les colonnes de type object
    obj_cols = df.select_dtypes(include="object").columns
    for c in obj_cols:
        df[c] = df[c].astype(str).str.strip()

    # nos colonnes de notes
    NOTE_COLS = [c for c in df.columns if "note" in c]

    for col in NOTE_COLS:
        df[col] = df[col].apply(_clean_numeric)

    return df
