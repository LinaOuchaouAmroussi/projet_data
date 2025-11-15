"""
Footer professionnel pour le dashboard
"""
from dash import html

def create_footer():
    """Crée un composant footer réutilisable avec design professionnel"""
    return html.Footer([
        # Container principal du footer
        html.Div([
            # Section des auteurs
            html.Div([
                html.H4(
                    "Auteurs", 
                    style={
                        'color': '#ffffff',
                        'fontFamily': 'Arial, sans-serif',
                        'fontSize': '18px',
                        'marginBottom': '15px',
                        'fontWeight': '600'
                    }
                ),
                html.Ul([
                    html.Li("OUCHAOU Lina", style={
                        'fontFamily': 'Arial, sans-serif',
                        'fontSize': '14px',
                        'marginBottom': '8px',
                        'color': '#e8eaf6'
                    }),
                    html.Li("POGEANT Justine", style={
                        'fontFamily': 'Arial, sans-serif',
                        'fontSize': '14px',
                        'marginBottom': '8px',
                        'color': '#e8eaf6'
                    }),
                ], style={
                    'listStyleType': 'none',
                    'padding': '0',
                    'margin': '0'
                })
            ], style={'margin': '20px', 'flex': '1'}),
            
            # Section des liens utiles
            html.Div([
                html.H4(
                    "Liens Utiles", 
                    style={
                        'color': '#ffffff',
                        'fontFamily': 'Arial, sans-serif',
                        'fontSize': '18px',
                        'marginBottom': '15px',
                        'fontWeight': '600'
                    }
                ),
                html.Ul([
                    html.Li(
                        html.A(
                            "📄 Documentation", 
                            href="https://www.data.gouv.fr/datasets/index-egalite-professionnelle-f-h-des-entreprises-de-50-salaries-ou-plus/", 
                            target="_blank",
                            style={
                                'color': '#e8eaf6',
                                'textDecoration': 'none',
                                'fontFamily': 'Arial, sans-serif',
                                'fontSize': '14px',
                                'transition': 'color 0.3s'
                            }
                        ),
                        style={'marginBottom': '8px'}
                    ),
                    html.Li(
                        html.A(
                            "💻 GitHub", 
                            href="https://github.com/LinaOuchaouAmroussi/projet_data.git", 
                            target="_blank",
                            style={
                                'color': '#e8eaf6',
                                'textDecoration': 'none',
                                'fontFamily': 'Arial, sans-serif',
                                'fontSize': '14px',
                                'transition': 'color 0.3s'
                            }
                        ),
                        style={'marginBottom': '8px'}
                    ),
                ], style={
                    'listStyleType': 'none',
                    'padding': '0',
                    'margin': '0'
                })
            ], style={'margin': '20px', 'flex': '1'}),
            
            # Section des informations du projet
            html.Div([
                html.H4(
                    "À Propos", 
                    style={
                        'color': '#ffffff',
                        'fontFamily': 'Arial, sans-serif',
                        'fontSize': '18px',
                        'marginBottom': '15px',
                        'fontWeight': '600'
                    }
                ),
                html.P(
                    "Dashboard créé dans le cadre du projet Python 2025",
                    style={
                        'fontFamily': 'Arial, sans-serif',
                        'fontSize': '14px',
                        'marginBottom': '8px',
                        'color': '#e8eaf6',
                        'lineHeight': '1.6'
                    }
                ),
                html.P(
                    "Données sources : Index Égalité Professionnelle",
                    style={
                        'fontFamily': 'Arial, sans-serif',
                        'fontSize': '14px',
                        'marginBottom': '0',
                        'color': '#e8eaf6',
                        'lineHeight': '1.6'
                    }
                )
            ], style={'margin': '20px', 'flex': '1'})
            
        ], style={
            'display': 'flex',
            'justifyContent': 'space-around',
            'alignItems': 'flex-start',
            'padding': '40px 20px',
            'backgroundColor': '#1f4788',  # Bleu foncé professionnel
            'color': 'white',
            'marginTop': '50px',
            'flexWrap': 'wrap'
        }),
        
        # Copyright
        html.Div([
            html.P(
                "© 2024-2025 Dashboard Égalité Professionnelle - Tous droits réservés", 
                style={
                    'textAlign': 'center',
                    'margin': '0',
                    'padding': '15px',
                    'fontFamily': 'Arial, sans-serif',
                    'fontSize': '13px',
                    'color': '#b0bec5'
                }
            )
        ], style={
            'backgroundColor': '#283593',  # Bleu foncé cohérent
            'borderTop': '1px solid #5c6bc0'
        })
    ], style={
        'width': '100%',
        'marginTop': 'auto'
    })


# CSS pour les effets hover (à ajouter dans votre app)
FOOTER_CSS = """
a:hover {
    color: #ffffff !important;
    text-decoration: underline !important;
}
"""