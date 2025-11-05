"""
Page du dashboard - Évolution des notes par taille d'entreprise
"""
import sys
from pathlib import Path

# Ajouter le projet au path
# Ajouter le projet au path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from dash import Dash, html, dcc
from src.components.component4 import create_size_evolution_plot

# Créer l'application
app = Dash(__name__)

# Définir le layout avec le graphique centré
app.layout = html.Div([
    # Container principal centré
    html.Div([
        # Titre
        html.H1(
            "📊 Évolution des Notes par Taille d'Entreprise",
            style={
                'textAlign': 'center',
                'color': '#1f4788',  # Bleu foncé
                'marginTop': '30px',
                'marginBottom': '10px',
                'fontFamily': 'Arial, sans-serif',
                'fontSize': '32px',
                'fontWeight': 'bold'
            }
        ),
        
        # Sous-titre
        html.P(
            "Animation de l'évolution des notes moyennes au fil des années",
            style={
                'textAlign': 'center',
                'fontSize': '18px',
                'color': '#2c3e50',
                'marginBottom': '10px',
                'fontFamily': 'Arial, sans-serif'
            }
        ),
        
        # Instructions
        html.P(
            "💡 Cliquez sur ▶️ pour lancer l'animation",
            style={
                'textAlign': 'center',
                'fontSize': '14px',
                'color': '#7f8c8d',
                'fontStyle': 'italic',
                'marginBottom': '40px',
                'fontFamily': 'Arial, sans-serif'
            }
        ),
        
        # Container du graphique centré
        html.Div([
            dcc.Graph(
                id='evolution-size-graph',
                figure=create_size_evolution_plot(),
                style={
                    'margin': '0 auto'  # Centre le graphique
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
    print("🚀 Lancement du Dashboard - Component 4")
    print("="*60)
    print("🌐 Ouvrez votre navigateur sur : http://127.0.0.1:8054/")
    print("⌨️  Appuyez sur Ctrl+C pour arrêter")
    print("="*60 + "\n")
    
    app.run(debug=True, port=8054)