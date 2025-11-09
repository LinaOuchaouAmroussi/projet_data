# main.py
import os
from src.utils.get_data import download_excel, convert_to_csv
from src.utils.clean_data import clean_data
from src.app import app
from config import DATA_RAW_PATH, DATA_CLEAN_PATH, DASHBOARD_PORT, DEBUG_MODE

def prepare_data():
    """Télécharge et nettoie les données si elles n’existent pas déjà."""
    if not os.path.exists(DATA_CLEAN_PATH):
        print("📥 Données nettoyées introuvables — génération en cours...")
        if not os.path.exists(DATA_RAW_PATH):
            print("📊 Téléchargement et conversion des données brutes...")
            download_excel()
            convert_to_csv()
        clean_data()
    else:
        print("✅ Données prêtes — aucun traitement nécessaire.")

if __name__ == "__main__":
    print("\n" + "="*70)
    print("🚀 LANCEMENT DU PIPELINE COMPLET")
    print("="*70)
    prepare_data()
    print("\n🎨 Lancement du dashboard...")
    print(f"🌐 URL : http://127.0.0.1:{DASHBOARD_PORT}/")
    print("="*70 + "\n")
    app.run(debug=DEBUG_MODE, port=DASHBOARD_PORT)
