"""
Page du dashboard - Statistiques clés
"""
import sys
from pathlib import Path
import dash
from dash import html, dcc

# Ajouter le projet au path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.components.component5 import create_stats_table

# Enregistrer cette page
dash.register_page(
    __name__,
    path='/component5',
    name=' Statistiques Clés'
)

# Définir le layout
layout = html.Div([

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
            " Statistiques Clés d'Égalité Professionnelle",
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