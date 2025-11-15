"""
Configuration globale du projet, de la base de donnée aux chemins de fichiers.
"""

from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

# nos dossiers
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
CLEAN_DIR = DATA_DIR / "cleaned"
WAREHOUSE_DIR = DATA_DIR / "warehouse"

# nos fichiers
DATA_RAW_PATH = RAW_DIR / "rawdata.csv"
DATA_CLEAN_CSV = CLEAN_DIR / "cleaneddata.csv"
DB_PATH = WAREHOUSE_DIR / "data.db"

# URL SQLAlchemy (corrige l'ImportError DB_URL)
DB_URL = f"sqlite:///{DB_PATH}"

# Engine global
engine = create_engine(DB_URL, future=True)

# Noms de tables
RAW_TABLE = "index_egalite_raw"
CLEAN_TABLE = "index_egalite_clean"

# On crée les dossiers si absents
for d in (RAW_DIR, CLEAN_DIR, WAREHOUSE_DIR):
    d.mkdir(parents=True, exist_ok=True)

# Nos colonnes clés
NOTE_COLUMNS = [
    "note_ecart_remuneration",
    "note_ecart_taux_d'augmentation_(hors_promotion)",
    "note_ecart_taux_de_promotion",
    "note_ecart_taux_d'augmentation",
    "note_retour_conge_maternite",
    "note_hautes_remunerations",
    "note_index"
]

SIZE_COLUMN = "tranche_d'effectifs"
YEAR_COLUMN = "annee"
REGION_COLUMN = "region"
DEPT_COLUMN = "departement"

# Fonction utilitaire: lire la table CLEAN depuis la base de donnée
def load_clean_df():
    try:
        return pd.read_sql(f"SELECT * FROM {CLEAN_TABLE}", con=engine)
    except Exception as e:
        print(f"ATTENTION : Impossible de charger {CLEAN_TABLE} : {e}")
        return pd.DataFrame()

# ➕ Crée un DataFrame df pour compatibilité avec la suite du projet
df = load_clean_df()   # ok ici car la table CLEAN existe après le pipeline dans main.py

