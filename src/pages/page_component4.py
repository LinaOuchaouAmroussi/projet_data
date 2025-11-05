"""
Page du dashboard - Évolution des notes par taille d'entreprise
"""
import sys
from pathlib import Path
import dash
from dash import html, dcc

# Ajouter le projet au path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.components.component4 import create_size_evolution_plot

# Enregistrer cette page
dash.register_page(
    __name__,
    path='/component4',
    name='📊 Évolution par Taille'
)

# Définir le layout avec le graphique centré
layout = html.Div([
    # Container principal centré
    html.Div([

        # Bouton retour
        html.Div([
            dcc.Link(
                '← Retour à l\'accueil',
                href='/',
                style={
                    'textDecoration': 'none',
                    'color': '#1f4788',
                    'fontSize': '16px',
                    'fontWeight': '500',
                    'fontFamily': 'Arial, sans-serif'
                }
            )
        ], style={'marginBottom': '20px'}),

        # Titre
        html.H1(
            "📊 Évolution des Notes par Taille d'Entreprise",
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