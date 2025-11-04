"""
Page du dashboard - Évolution temporelle animée par région
"""
import sys
from pathlib import Path

# Ajouter le projet au path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from dash import Dash, html, dcc
from src.components.component3 import create_temporal_evolution_plot

# Créer l'application
app = Dash(__name__)

# Définir le layout
app.layout = html.Div([
    html.H1(
        "📈 Évolution Temporelle des Notes d'Égalité Professionnelle",
        style={'textAlign': 'center', 'color': '#FF6B6B', 'marginTop': '20px'}
    ),
    html.P(
        "Animation de l'évolution des notes par année et par région",
        style={'textAlign': 'center', 'fontSize': '18px', 'color': '#666', 'marginBottom': '10px'}
    ),
    html.P(
        "💡 Cliquez sur ▶️ pour lancer l'animation",
        style={'textAlign': 'center', 'fontSize': '14px', 'color': '#999', 'fontStyle': 'italic', 'marginBottom': '30px'}
    ),
    html.Div([
        dcc.Graph(
            id='temporal-evolution-graph',
            figure=create_temporal_evolution_plot()
        )
    ], style={'padding': '20px'})
])

# Lancer le serveur
if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Lancement du Dashboard - Component 3")
    print("="*60)
    print("🌐 Ouvrez votre navigateur sur : http://127.0.0.1:8053/")
    print("⌨️  Appuyez sur Ctrl+C pour arrêter")
    print("="*60 + "\n")
    
    app.run(debug=True, port=8053)