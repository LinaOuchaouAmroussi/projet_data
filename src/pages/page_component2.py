"""
Page du dashboard - Notes moyennes par taille d'entreprise
"""
import sys
from pathlib import Path

# Ajouter le projet au path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from dash import Dash, html, dcc
from src.components.component2 import create_size_distribution_plot

# Créer l'application
app = Dash(__name__)

# Définir le layout
app.layout = html.Div([
    html.H1(
        "📊 Note Moyenne d'Égalité Professionnelle par Taille d'Entreprise",
        style={'textAlign': 'center', 'color': '#0074D9', 'marginTop': '20px'}
    ),
    html.P(
        "Cette page montre la note moyenne globale par tranche de taille d'entreprise.",
        style={'textAlign': 'center', 'fontSize': '18px', 'color': '#666', 'marginBottom': '30px'}
    ),
    html.Div([
        dcc.Graph(
            id='size-distribution-graph',
            figure=create_size_distribution_plot()
        )
    ], style={'padding': '20px'})
])

# Lancer le serveur
if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Lancement du Dashboard - Component 2")
    print("="*60)
    print("🌐 Ouvrez votre navigateur sur : http://127.0.0.1:8052/")
    print("⌨️  Appuyez sur Ctrl+C pour arrêter")
    print("="*60 + "\n")
    
    app.run(debug=True, port=8052)