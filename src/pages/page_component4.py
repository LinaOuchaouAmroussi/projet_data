"""
Page du dashboard - Évolution par taille d'entreprise
"""
import sys
from pathlib import Path

# Ajouter le projet au path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from dash import Dash, html, dcc

# Import du composant - IMPORTANT: avec src.
from src.components.component4 import create_size_evolution_plot

# Créer l'application
app = Dash(__name__)

# Définir le layout
app.layout = html.Div([
    html.H1(
        "📈 Évolution des Notes par Taille d'Entreprise", 
        style={'textAlign': 'center', 'color': '#7FDBFF', 'marginTop': '20px'}
    ),
    html.Div([
        dcc.Graph(
            id='size-evolution-plot',
            figure=create_size_evolution_plot()
        )
    ], style={'padding': '20px'}),
    html.Div([
        html.P("Utilisez les contrôles d'animation pour voir l'évolution temporelle",
               style={'textAlign': 'center', 'fontStyle': 'italic'})
    ], style={'marginTop': '10px'})
])

# Lancer le serveur
if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Lancement du Dashboard")
    print("="*60)
    print("🌐 Ouvrez votre navigateur sur : http://127.0.0.1:8054/")
    print("⌨️  Appuyez sur Ctrl+C pour arrêter")
    print("="*60 + "\n")
    
    app.run(debug=True, port=8054)