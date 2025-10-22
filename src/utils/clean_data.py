# src/utils/clean_data.py
import os
import pandas as pd

# Chemin absolu vers le dossier projet_data
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Chemins d'accès à partir du dossier projet_data
RAW_DIR = os.path.join(PROJECT_DIR, "data", "raw")
CLEAN_DIR = os.path.join(PROJECT_DIR, "data", "cleaned")

RAW_FILE = os.path.join(RAW_DIR, "rawdata.csv")
CLEAN_FILE = os.path.join(CLEAN_DIR, "cleaneddata.csv")

def clean_data():
    """Nettoie les données CSV et les enregistre dans data/cleaned/"""
    os.makedirs(CLEAN_DIR, exist_ok=True)

    print("Lecture du fichier brut...")
    df = pd.read_csv(RAW_FILE)

    print("Nettoyage des données...")
    # Ne pas supprimer toutes les lignes avec NA
    # Au lieu de ça, on peut :
    df = df.fillna("NC")  # Remplacer les NA par "NC"
    df = df.drop_duplicates()  # Supprimer les doublons
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    print("Sauvegarde du fichier nettoyé...")
    df.to_csv(CLEAN_FILE, index=False)
    print(f"Données nettoyées enregistrées dans {CLEAN_FILE}")

if __name__ == "__main__":
    clean_data()

