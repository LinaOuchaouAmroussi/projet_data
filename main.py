"""
Notre fichier main qui contient le pipeline complet :
1. on charge rawdata.csv
2. on insère dans la table RAW
3. on nettoie les données
4. on insère la table CLEAN
5. on lance l'app
"""

from config import DATA_RAW_PATH, DATA_CLEAN_CSV, RAW_TABLE, CLEAN_TABLE
import pandas as pd
from src.utils.clean_data import clean_data
from src.utils.db import write_raw_to_db, write_clean_to_db, load_clean_df

print("Pipeline DB : nettoyage + insertion")

# On charge le CSV brut
print("Chargement du CSV brut…")
df_raw = pd.read_csv(DATA_RAW_PATH)

# On insère la table RAW dans SQLite
print("Insertion dans la table RAW…")
write_raw_to_db(df_raw, table=RAW_TABLE)

# Nettoyage -> DataFrame propre
print("Nettoyage…")
df_clean = clean_data()

# 4️-on écrit la table CLEAN dans la base
print("Écriture table CLEAN…")
write_clean_to_db(df_clean, table=CLEAN_TABLE)

# On charge le dataframe propre pour le dashboard
df = load_clean_df()

# on lance notre app
from src.app import app

if __name__ == "__main__":
    app.run(debug=True)
