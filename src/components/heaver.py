from dash import html

def create_header():
    """Crée un composant header réutilisable avec navigation et titre"""
    return html.Header([
        # Barre de navigation
        html.Nav([
            # Logo ou titre principal
            html.Div([
                html.H1("Dashboard Égalité Professionnelle",
                       style={
                           'margin': '0',
                           'color': '#7FDBFF',
                           'fontSize': '24px'
                       })
            ], style={'flex': '1'}),
            
            # Menu de navigation
            html.Ul([
                html.Li(html.A("Accueil", href="#"),
                       style={'display': 'inline', 'margin': '0 15px'}),
                html.Li(html.A("Statistiques", href="#distribution"),
                       style={'display': 'inline', 'margin': '0 15px'}),
                html.Li(html.A("Évolution", href="#evolution"),
                       style={'display': 'inline', 'margin': '0 15px'}),
                html.Li(html.A("À propos", href="#about"),
                       style={'display': 'inline', 'margin': '0 15px'}),
            ], style={
                'listStyleType': 'none',
                'margin': '0',
                'padding': '0',
                'display': 'flex',
                'alignItems': 'center'
            })
        ], style={
            'display': 'flex',
            'alignItems': 'center',
            'padding': '20px',
            'backgroundColor': '#1A1A1A',
            'color': 'white'
        }),
        
        # Sous-header avec description
        html.Div([
            html.P("""
                Analyse de l'Index de l'Égalité Professionnelle en France.
                Visualisation des données sur les écarts de rémunération et 
                l'évolution des notes par entreprise.
            """,
            style={
                'margin': '0',
                'textAlign': 'center',
                'padding': '15px'
            })
        ], style={
            'backgroundColor': '#2C2C2C',
            'color': '#DDD',
            'padding': '10px'
        })
    ], style={
        'position': 'sticky',
        'top': '0',
        'zIndex': '1000',
        'boxShadow': '0 2px 4px rgba(0,0,0,0.2)'
    })