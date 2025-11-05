"""
Page du dashboard - Statistiques clés
"""
import sys
from pathlib import Path

# Ajouter le projet au path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from dash import Dash, html, dcc

# Import du composant - IMPORTANT: avec src.
from src.components.component5 import create_stats_table

# Créer l'application
app = Dash(__name__)

# Définir le layout
app.layout = html.Div([
    html.H5(
        "🧮 Statistiques Clés d'Égalité Professionnelle", 
        style={'textAlign': 'center', 'color': '#7FDBFF', 'marginTop': '20px'}
    ),
    html.Div([
        dcc.Graph(
            id='stats-table',
            figure=create_stats_table()
        )
    ], style={'padding': '20px'})
])

# Lancer le serveur
if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Lancement du Dashboard")
    print("="*60)
    print("🌐 Ouvrez votre navigateur sur : http://127.0.0.1:8055/")
    print("⌨️  Appuyez sur Ctrl+C pour arrêter")
    print("="*60 + "\n")
    
    app.run(debug=True, port=8055)

