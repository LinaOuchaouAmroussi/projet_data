"""
Page du dashboard - Distribution des notes
"""
import sys
from pathlib import Path

# Ajouter le projet au path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from dash import Dash, html, dcc
from src.components.component1 import create_distribution_plot

# Créer l'application
app = Dash(__name__)

# Définir le layout
app.layout = html.Div([
    
    # Container principal centré
    html.Div([
        
        # Titre
        html.H1(
            "📊 Distribution des Notes d'Égalité Professionnelle", 
            style={
                'textAlign': 'center',
                'color': '#1f4788',  
                'marginTop': '30px',
                'marginBottom': '10px',
                'fontFamily': 'Arial, sans-serif',
                'fontSize': '32px',
                'fontWeight': 'bold'
            }
        ),

        # Sous-titre
        html.P(
            "Répartition des notes calculées parmi les entreprises.",
            style={
                'textAlign': 'center',
                'fontSize': '18px',
                'color': '#2c3e50',
                'marginBottom': '40px',
                'fontFamily': 'Arial, sans-serif'
            }
        ),

        # Graphique centré
        html.Div([
            dcc.Graph(
                id='distribution-plot',
                figure=create_distribution_plot(),
                style={
                    'margin': '0 auto'
                }
            )
        ], style={
            'display': 'flex',
            'justifyContent': 'center',
            'alignItems': 'center',
            'padding': '20px'
        })

    ], style={
        'maxWidth': '1200px',
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
    print("🚀 Lancement du Dashboard - Component 1")
    print("="*60)
    print("🌐 Ouvrez votre navigateur sur : http://127.0.0.1:8051/")
    print("⌨️  Appuyez sur Ctrl+C pour arrêter")
    print("="*60 + "\n")
    
    app.run(debug=True, port=8051)
