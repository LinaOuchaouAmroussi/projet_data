"""
Page du dashboard - Carte interactive de l’égalité professionnelle
"""
import sys
from pathlib import Path

# --- Ajouter le projet au path (important pour import src) ---
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# --- Imports Dash et composant ---
from dash import Dash, html
from src.components.component_map import create_map  # fonction qui crée la carte

# --- Création de l’application Dash ---
app = Dash(__name__)
app.title = "Dashboard Égalité Professionnelle"

# --- Layout ---
app.layout = html.Div([
    html.H1(
        "🗺️ Carte de l'égalité professionnelle par département",
        style={'textAlign': 'center', 'color': '#003366', 'marginTop': '20px'}
    ),

    html.Div(
        id='map-container',
        children=[
            html.Iframe(
                id='map',
                srcDoc=create_map(),  # on appelle la fonction importée
                width='100%',
                height='650'
            )
        ],
        style={
            'padding': '20px',
            'border': '1px solid #ddd',
            'borderRadius': '10px'
        }
    ),

    html.Div(
        "Cette carte affiche la note moyenne d’égalité professionnelle par département.",
        style={'textAlign': 'center', 'marginTop': '20px', 'fontSize': '18px'}
    )
])

# --- Lancement ---
if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Lancement du Dashboard")
    print("="*60)
    print("🌐 Ouvrez votre navigateur sur : http://127.0.0.1:8056/")
    print("⌨️  Appuyez sur Ctrl+C pour arrêter")
    print("="*60 + "\n")

    app.run(debug=True, port=8056)
