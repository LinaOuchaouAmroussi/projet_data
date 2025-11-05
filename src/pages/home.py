"""
Page d'accueil du Dashboard
Affiche les liens vers toutes les analyses disponibles
"""
import dash
from dash import html, dcc

# Enregistrer cette page comme page d'accueil
dash.register_page(
    __name__,
    path='/',  # URL : http://127.0.0.1:8050/
    name='🏠 Accueil'
)

# Contenu de la page d'accueil
layout = html.Div([
    
    # Titre principal
    html.H1(
        "🏠 Tableau de Bord - Égalité Professionnelle",
        style={
            'textAlign': 'center',
            'color': '#2c3e50',
            'marginTop': '30px',
            'marginBottom': '20px'
        }
    ),
    
    # Sous-titre
    html.P(
        "Sélectionnez une analyse pour explorer les données",
        style={
            'textAlign': 'center',
            'fontSize': '1.2rem',
            'color': '#7f8c8d',
            'marginBottom': '50px'
        }
    ),
    
    # Grille de cartes pour chaque page
    html.Div([
        
        # Carte Component 2
        html.Div([
            dcc.Link([
                html.Div([
                    html.H3("📊 Distribution par Taille", style={'margin': '0 0 10px 0'}),
                    html.P("Note moyenne d'égalité par taille d'entreprise")
                ])
            ], href='/component2', style={'textDecoration': 'none', 'color': 'inherit'})
        ], style={
            'backgroundColor': '#3498db',
            'color': 'white',
            'padding': '30px',
            'borderRadius': '10px',
            'boxShadow': '0 4px 6px rgba(0,0,0,0.1)',
            'cursor': 'pointer',
            'transition': 'transform 0.3s'
        }),
        
        # Carte Component 3
        html.Div([
            dcc.Link([
                html.Div([
                    html.H3("📈 Analyse Component 3", style={'margin': '0 0 10px 0'}),
                    html.P("Description de ton component 3")
                ])
            ], href='/component3', style={'textDecoration': 'none', 'color': 'inherit'})
        ], style={
            'backgroundColor': '#2ecc71',
            'color': 'white',
            'padding': '30px',
            'borderRadius': '10px',
            'boxShadow': '0 4px 6px rgba(0,0,0,0.1)',
            'cursor': 'pointer',
            'transition': 'transform 0.3s'
        }),
        
        # Carte Component 4
        html.Div([
            dcc.Link([
                html.Div([
                    html.H3("📉 Analyse Component 4", style={'margin': '0 0 10px 0'}),
                    html.P("Description de ton component 4")
                ])
            ], href='/component4', style={'textDecoration': 'none', 'color': 'inherit'})
        ], style={
            'backgroundColor': '#e74c3c',
            'color': 'white',
            'padding': '30px',
            'borderRadius': '10px',
            'boxShadow': '0 4px 6px rgba(0,0,0,0.1)',
            'cursor': 'pointer',
            'transition': 'transform 0.3s'
        }),
        
        # Ajoute d'autres cartes pour tes autres components...
        
    ], style={
        'display': 'grid',
        'gridTemplateColumns': 'repeat(auto-fit, minmax(300px, 1fr))',
        'gap': '30px',
        'maxWidth': '1200px',
        'margin': '0 auto',
        'padding': '20px'
    })
])
