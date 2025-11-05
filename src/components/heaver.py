"""
Header commun avec menu déroulant cliquable
"""
from dash import html, dcc

def create_header():
    """
    Crée le header avec un bouton ouvrant un menu déroulant
    """
    return html.Div([
        
        # Conteneur principal
        html.Div([
            
            # Logo et titre (à gauche)
            html.Div([
                dcc.Link(
                    "🏠 Dashboard Égalité Professionnelle",
                    href="/",
                    style={
                        'color': 'white',
                        'textDecoration': 'none',
                        'fontSize': '24px',
                        'fontWeight': 'bold'
                    }
                )
            ], style={'flex': '1'}),
            
            # Menu déroulant (à droite)
            html.Div([
                
                # Bouton pour ouvrir le menu
                html.Button(
                    "📊 Pages ▼",
                    id="menu-button",
                    n_clicks=0,
                    style={
                        'backgroundColor': 'rgba(255, 255, 255, 0.2)',
                        'color': 'white',
                        'border': '2px solid white',
                        'borderRadius': '8px',
                        'padding': '10px 20px',
                        'fontSize': '16px',
                        'fontWeight': 'bold',
                        'cursor': 'pointer',
                        'transition': 'all 0.3s ease'
                    }
                ),
                
                # Menu déroulant (caché par défaut)
                html.Div([
                    
                    dcc.Link(
                        "📊 Distribution des Notes",
                        href="/component1",
                        className="dropdown-item"
                    ),
                    
                    html.Hr(style={'margin': '5px 0', 'borderColor': '#ddd'}),
                    
                    dcc.Link(
                        "📊 Notes par Taille d'Entreprise",
                        href="/component2",
                        className="dropdown-item"
                    ),
                    
                    html.Hr(style={'margin': '5px 0', 'borderColor': '#ddd'}),
                    
                    dcc.Link(
                        "📈 Évolution Temporelle",
                        href="/component3",
                        className="dropdown-item"
                    ),
                    
                    html.Hr(style={'margin': '5px 0', 'borderColor': '#ddd'}),
                    
                    dcc.Link(
                        "📊 Évolution par Taille",
                        href="/component4",
                        className="dropdown-item"
                    ),
                    
                    html.Hr(style={'margin': '5px 0', 'borderColor': '#ddd'}),
                    
                    dcc.Link(
                        "🧮 Statistiques Clés",
                        href="/component5",
                        className="dropdown-item"
                    ),
                    
                    html.Hr(style={'margin': '5px 0', 'borderColor': '#ddd'}),
                    
                    dcc.Link(
                        "🗺️ Carte Interactive",
                        href="/map",
                        className="dropdown-item"
                    )
                    
                ], id="dropdown-menu", style={
                    'display': 'none',  # Caché par défaut
                    'position': 'absolute',
                    'top': '100%',
                    'right': '0',
                    'marginTop': '10px',
                    'backgroundColor': 'white',
                    'borderRadius': '8px',
                    'boxShadow': '0 4px 12px rgba(0,0,0,0.15)',
                    'minWidth': '280px',
                    'padding': '10px 0',
                    'zIndex': '1000'
                })
                
            ], style={
                'position': 'relative'  # Important pour le positionnement absolu du menu
            })
            
        ], style={
            'display': 'flex',
            'alignItems': 'center',
            'maxWidth': '1400px',
            'margin': '0 auto',
            'padding': '0 20px'
        })
        
    ], style={
        'backgroundColor': '#1f4788',
        'padding': '15px 0',
        'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
        'position': 'sticky',
        'top': '0',
        'zIndex': '999'
    })
