import os
import requests
import pandas as pd

"""
Module de récuperation des données brutes venant de l'url https://www.data.gouv.fr/api/1/datasets/r/d434859f-8d3b-4381-bcdb-ec9200653ae6.
Télecharge le fichier Excel de données et le convertit en CSV.
Etape préliminaire avant l'insertion et le nettoyage en base de données.
"""

# URL du fichier Excel sur data.gouv.fr
DATA_URL = "https://www.data.gouv.fr/api/1/datasets/r/d434859f-8d3b-4381-bcdb-ec9200653ae6"

# Chemin absolu vers le dossier projet_data
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Chemins d'accès à partir du dossier projet_data
RAW_DIR = os.path.join(PROJECT_DIR, "data", "raw")
EXCEL_PATH = os.path.join(RAW_DIR, "rawdata.xlsx")
CSV_PATH = os.path.join(RAW_DIR, "rawdata.csv")

def download_excel():
    """Télécharge le fichier Excel brut dans data/raw/"""
    os.makedirs(RAW_DIR, exist_ok=True)
    print("Téléchargement du fichier Excel...")

    response = requests.get(DATA_URL)
    if response.status_code == 200:
        with open(EXCEL_PATH, "wb") as f:
            f.write(response.content)
        print(f"Fichier téléchargé dans {EXCEL_PATH}")
    else:
        raise Exception(f"Échec du téléchargement (code {response.status_code})")

def convert_to_csv():
    """Convertit le fichier Excel téléchargé en CSV"""
    print("Conversion du fichier Excel en CSV...")
    # Spécifier explicitement le moteur 'openpyxl' pour les fichiers .xlsx
    df = pd.read_excel(EXCEL_PATH, engine='openpyxl')
    df.to_csv(CSV_PATH, index=False)
    print(f"Fichier converti et enregistré sous {CSV_PATH}")

def main():
    download_excel()
    convert_to_csv()

if __name__ == "__main__":
    main()
