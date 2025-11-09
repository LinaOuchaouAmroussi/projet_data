"""
Page du dashboard - Distribution des notes
"""
import sys
from pathlib import Path
import dash
from dash import html, dcc

# Ajouter le projet au path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.components.component1 import create_distribution_plot

# Enregistrer cette page
dash.register_page(
    __name__,
    path='/component1',
    name=' Distribution des Notes'
)

# Définir le layout
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
            " Distribution des Notes d'Égalité Professionnelle", 
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