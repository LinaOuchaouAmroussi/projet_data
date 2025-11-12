# -*- coding: utf-8 -*-
"""
Configuration globale du projet Data Dashboard.

Ce module définit les chemins d'accès aux données, charge le DataFrame principal
et configure les paramètres globaux du dashboard d'égalité professionnelle.
"""

# ============================================================
# 📁 config.py — Configuration globale du projet Data Dashboard
# ============================================================

import os
import pandas as pd

# ------------------------------------------------------------
# 🧭 CHEMINS DE BASE
# ------------------------------------------------------------
# Répertoire racine du projet (ex: /Users/nom/data_project)
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Dossiers de données
DATA_DIR = os.path.join(PROJECT_DIR, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw")
CLEAN_DIR = os.path.join(DATA_DIR, "cleaned")

# Fichiers de données
DATA_RAW_PATH = os.path.join(RAW_DIR, "rawdata.csv")
DATA_CLEAN_PATH = os.path.join(CLEAN_DIR, "cleaneddata.csv")

# ------------------------------------------------------------
# 📦 DONNÉES PRINCIPALES
# ------------------------------------------------------------
# On charge les données nettoyées une seule fois au démarrage.
# Ce DataFrame est ensuite partagé par tous les composants Dash.
try:
    df = pd.read_csv(DATA_CLEAN_PATH)
    print(f"✅ Données chargées depuis : {DATA_CLEAN_PATH}")
except FileNotFoundError:
    print(f"⚠️  Fichier nettoyé introuvable à {DATA_CLEAN_PATH}.")
    print(
        "   Lancez `main.py` pour télécharger/nettoyer les données "
        "avant de démarrer le dashboard."
    )
    df = pd.DataFrame()  # dataframe vide pour éviter les plantages

# ------------------------------------------------------------
# 📊 CONFIGURATION DES COLONNES UTILISÉES DANS LES GRAPHIQUES
# ------------------------------------------------------------
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
DEPT_COLUMN = 'département'

# ------------------------------------------------------------
# ⚙️ PARAMÈTRES GLOBAUX DU DASHBOARD
# ------------------------------------------------------------
DASHBOARD_TITLE = "Dashboard Égalité Professionnelle"
DASHBOARD_PORT = 8051
DEBUG_MODE = True

# ------------------------------------------------------------
# 📁 AUTRES PARAMÈTRES (optionnels)
# ------------------------------------------------------------
# Exemple : lien vers le fichier GeoJSON pour les cartes
DEPARTEMENTS_GEOJSON = os.path.join(RAW_DIR, "departements.json")

# ------------------------------------------------------------
# ✅ UTILISATION :
# ------------------------------------------------------------
# from config import df, NOTE_COLUMNS, DATA_CLEAN_PATH
# from config import DASHBOARD_PORT, DEBUG_MODE
# ------------------------------------------------------------
# Fin de config.py
# ------------------------------------------------------------
