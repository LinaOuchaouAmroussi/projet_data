from dash import html

def create_footer():
    """Crée un composant footer réutilisable"""
    return html.Footer([
        # Container principal du footer
        html.Div([
            # Section des auteurs
            html.Div([
                html.H4("Auteurs", style={'color': "#0B0E4E"}),
                html.Ul([
                    html.Li("OUCHAOU Lina"),
                    html.Li("POGEANT Justine"),
                ], style={'listStyleType': 'none'})
            ], style={'margin': '20px'}),
            
            # Section des liens utiles
            html.Div([
                html.H4("Liens Utiles", style={'color': '#7FDBFF'}),
                html.Ul([
                    html.Li(html.A("Documentation", href="https://www.data.gouv.fr/", target="_blank")),
                    html.Li(html.A("GitHub", href="https://github.com/votre-repo", target="_blank")),
                ], style={'listStyleType': 'none'})
            ], style={'margin': '20px'}),
            
            # Section des informations du projet
            html.Div([
                html.H4("À Propos", style={'color': '#7FDBFF'}),
                html.P("Dashboard créé dans le cadre du projet Python 2025"),
                html.P("Données sources : Index Égalité Professionnelle")
            ], style={'margin': '20px'})
            
        ], style={
            'display': 'flex',
            'justifyContent': 'space-around',
            'padding': '20px',
            'backgroundColor': "#0E63E2",
            'color': 'white',
            'marginTop': '50px'
        }),
        
        # Copyright
        html.Div([
            html.P("© 2024 - Tous droits réservés", 
                  style={'textAlign': 'center', 'margin': '10px'})
        ], style={
            'backgroundColor': '#0F0F0F',
            'color': '#888',
            'padding': '10px'
        })
    ])