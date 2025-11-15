"""
Page du dashboard - Carte interactive de l'égalité professionnelle
"""
import sys
from pathlib import Path
import dash
from dash import html

# Ajouter le projet au path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.components.component_map import create_map

# Enregistrer cette page
dash.register_page(
    __name__,
    path='/map',
    name=' Carte Interactive'
)

# Layout
layout = html.Div([

    # Bouton retour
    html.Div([
        html.A(
            '← Retour à l\'accueil',
            href='/',
            style={
                'textDecoration': 'none',
                'color': '#003366',
                'fontSize': '16px',
                'fontWeight': '500',
                'display': 'inline-block',
                'marginBottom': '20px',
                'marginLeft': '20px',
                'marginTop': '20px'
            }
        )
    ]),

    html.H1(
        " Carte de l'égalité professionnelle par département",
        style={'textAlign': 'center',
               'color': '#003366',
               'marginTop': '20px',
               'fontFamily': 'Arial, sans-serif'}
    ),

    html.Div(
        id='map-container',
        children=[
            html.Iframe(
                id='map',
                srcDoc=create_map(),
                width='100%',
                height='650'
            )
        ],
        style={
            'padding': '20px',
            'border': '1px solid #ddd',
            'borderRadius': '10px'
        }
    ),

    html.Div(
        "Cette carte affiche la note moyenne d'égalité professionnelle par département.",
        style={'textAlign': 'center',
               'marginTop': '20px', 
               'fontSize': '18px',
               'fontFamily': 'Arial, sans-serif'}
    )
])
