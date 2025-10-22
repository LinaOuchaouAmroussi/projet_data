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
    df = pd.read_csv(RAW_FILE, low_memory=False)  # Ajout de low_memory=False pour éviter l'avertissement

    print("Nettoyage des données...")
    # Remplir les valeurs manquantes
    # Colonnes numériques à traiter
    numeric_columns = [
        'Note Ecart rémunération',
        'Note Ecart taux d\'augmentation (hors promotion)',
        'Note Ecart taux de promotion',
        'Note Ecart taux d\'augmentation',
        'Note Retour congé maternité',
        'Note Hautes rémunérations',
        'Note Index'
    ]

    # Remplacer les valeurs vides par NaN pour les colonnes numériques
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Remplacer les valeurs manquantes par "NC" pour les colonnes texte
    text_columns = [col for col in df.columns if col not in numeric_columns]
    
    # Supprimer les doublons
    df = df.drop_duplicates()
    
    # Nettoyer les noms de colonnes
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    
    print("Sauvegarde du fichier nettoyé...")
    df.to_csv(CLEAN_FILE, index=False)
    print(f"Données nettoyées enregistrées dans {CLEAN_FILE}")

if __name__ == "__main__":
    clean_data()

