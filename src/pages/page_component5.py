"""
Page du dashboard - Statistiques clés
"""
import sys
from pathlib import Path

# Ajouter le projet au path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from dash import Dash, html, dcc
from src.components.component5 import create_stats_table

# Créer l'application
app = Dash(__name__)

# Définir le layout
app.layout = html.Div([
    
    html.Div([
        
        # Titre
        html.H1(
            "🧮 Statistiques Clés d'Égalité Professionnelle",
            style={
                'textAlign': 'center',
                'color': '#1f4788',
                'marginTop': '30px',
                'marginBottom': '40px',
                'fontFamily': 'Arial, sans-serif',
                'fontSize': '32px',
                'fontWeight': 'bold'
            }
        ),

        # Tableau pleine largeur, sans scroll
        dcc.Graph(
            id='stats-table',
            figure=create_stats_table(),
            style={
                'width': '100%',
                'margin': '0 auto'
            }
        )

    ], style={
        'maxWidth': '1400px',
        'margin': '0 auto',
        'padding': '20px',
        'fontFamily': 'Arial, sans-serif'
    })

], style={
    'backgroundColor': '#f8f9fa',
    'minHeight': '100vh',
    'fontFamily': 'Arial, sans-serif'
})

# Lancer le serveur
if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Lancement du Dashboard - Component 5")
    print("="*60)
    print("🌐 Ouvrez votre navigateur sur : http://127.0.0.1:8055/")
    print("⌨️  Appuyez sur Ctrl+C pour arrêter")
    print("="*60 + "\n")
    
    app.run(debug=True, port=8055)
