"""
Notre moteur de notre base de donnée.
Contient des fonctions pour lire et écrire les données nettoyées dans SQLite.
"""

import pandas as pd
from sqlalchemy import create_engine
from config import DB_URL, CLEAN_TABLE, DATA_CLEAN_CSV

# On crée un engin centralisé
engine = create_engine(DB_URL, future=True)

# On charge le CSV CLEAN tel quel (sans normalisation)
def load_clean_csv(csv_path=DATA_CLEAN_CSV):
    return pd.read_csv(csv_path, low_memory=False)

# On écrit le CLEAN dans SQLite sans modifier les noms de colonnes
def write_clean_to_db(df: pd.DataFrame, table: str = CLEAN_TABLE):
    # to_sql ne modifie pas les en-têtes si index=False
    df.to_sql(table, engine, if_exists="replace", index=False)


def write_raw_to_db(df, table):
    df.to_sql(table, con=engine, if_exists="replace", index=False)


# On vérifie que la table de la base de donnée a bien les mêmes colonnes que le CSV
def assert_db_matches_csv(df_csv: pd.DataFrame, table: str = CLEAN_TABLE):
    df_db = pd.read_sql(f"SELECT * FROM {table} LIMIT 0", con=engine)
    assert list(df_db.columns) == list(df_csv.columns), \
        f"Noms de colonnes modifiés ! CSV={list(df_csv.columns)} DB={list(df_db.columns)}"

# On lit la table CLEAN depuis SQLite (utilisé par l’app)
def load_clean_df(table: str = CLEAN_TABLE):
    try:
        return pd.read_sql(f"SELECT * FROM {table}", con=engine)
    except Exception as e:
        print(f"ATTENTION : Impossible de charger {table} : {e}")
        return pd.DataFrame()
