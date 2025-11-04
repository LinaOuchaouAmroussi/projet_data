import os
import pandas as pd

# Chemin absolu vers le dossier projet_data
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Chemins d'accès
CLEANED_DATA = os.path.join(PROJECT_DIR, "data", "cleaned", "cleaneddata.csv")

# Configuration des colonnes
NOTE_COLUMNS = [
    'note_ecart_rémunération',
    'note_ecart_taux_d\'augmentation_(hors_promotion)',
    'note_ecart_taux_de_promotion',
    'note_ecart_taux_d\'augmentation',
    'note_retour_congé_maternité',
    'note_hautes_rémunérations',
    'note_index'
]

SIZE_COLUMN = 'tranche_d\'effectifs'
YEAR_COLUMN = 'année'
REGION_COLUMN = 'région'

# Charger les données une seule fois
df = pd.read_csv(CLEANED_DATA)