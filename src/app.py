"""
Application principale du Dashboard - Égalité Professionnelle
Point d'entrée unique pour toutes les pages
"""
import sys
from pathlib import Path
from dash import Dash, html
import dash

# Ajouter le projet au path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Importer tes composants communs
from src.components.heaver import create_header
from src.components.footer import create_footer

# Créer l'application avec support multi-pages
app = Dash(
    __name__,
    use_pages=True,  # Active le système multi-pages
    suppress_callback_exceptions=True
)

# Titre de l'application
app.title = "Dashboard Égalité Professionnelle"

# Layout principal : Header + Contenu des pages + Footer
app.layout = html.Div([
    
    # Header commun (affiché sur toutes les pages)
    create_header(),
    
    # Conteneur pour le contenu de chaque page
    # C'est ici que s'afficheront home.py, page_component2.py, etc.
    html.Div([
        dash.page_container
    ], style={
        'minHeight': '70vh',
        'padding': '20px',
        'backgroundColor': '#f8f9fa'
    }),
    
    # Footer commun (affiché sur toutes les pages)
    create_footer()
    
])

@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(path):
    if path == "/page1":
        from page_component1 import app as page
        return page.layout
    elif path == "/page2":
        from page_component2 import app as page
        return page.layout
    elif path == "/page3":
        from page_component3 import app as page
        return page.layout
    elif path == "/page4":
        from page_component4 import app as page
        return page.layout
    elif path == "/page5":
        from page_component5 import app as page
        return page.layout
    return html.H1("Bienvenue sur le Dashboard 👋", style={"textAlign": "center", "marginTop": "50px"})

@app.callback(Output("url", "pathname"), Input("page-selector", "value"))
def navigate(value):
    return value if value else "/"

# Lancement du serveur
if __name__ == '__main__':
    print("\n" + "="*70)
    print("DASHBOARD ÉGALITÉ PROFESSIONNELLE")
    print("="*70)
    print("Ouvrez votre navigateur sur : http://127.0.0.1:8051/")
    print("Appuyez sur Ctrl+C pour arrêter le serveur")
    print("="*70 + "\n")
    
    app.run(debug=True, port=8051)