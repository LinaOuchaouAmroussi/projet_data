"""
Application principale avec menu déroulant interactif
"""
import sys
from pathlib import Path
from dash import Dash, html, dcc, Input, Output, State
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
    use_pages=True,
    suppress_callback_exceptions=True
)

# Titre de l'application
app.title = "Dashboard Égalité Professionnelle"

# Layout principal
app.layout = html.Div([

    # Header avec menu déroulant
    create_header(),

    # Conteneur pour le contenu de chaque page
    html.Div([
        dash.page_container
    ], style={
        'minHeight': '70vh',
        'padding': '20px',
        'backgroundColor': '#f8f9fa'
    }),

    # Footer commun
    create_footer()

])

# ✨ CALLBACK pour ouvrir/fermer le menu déroulant
@app.callback(
    Output('dropdown-menu', 'style'),
    Output('menu-button', 'children'),
    Input('menu-button', 'n_clicks'),
    State('dropdown-menu', 'style')
)
def toggle_dropdown(n_clicks, current_style):
    """
    Ouvre ou ferme le menu au clic sur le bouton
    """
    if n_clicks and n_clicks % 2 == 1:  # Menu ouvert
        current_style['display'] = 'block'
        button_text = "📊 Pages ▲"
    else:  # Menu fermé
        current_style['display'] = 'none'
        button_text = "📊 Pages ▼"
    
    return current_style, button_text

# Lancement du serveur
if __name__ == '__main__':
    print("\n" + "="*70)
    print("🚀 DASHBOARD ÉGALITÉ PROFESSIONNELLE")
    print("="*70)
    
    # Afficher les pages détectées
    if dash.page_registry:
        print("📄 Pages disponibles :")
        for page in dash.page_registry.values():
            print(f"   • {page['name']}: http://127.0.0.1:8051{page['path']}")
    else:
        print("⚠️  AUCUNE PAGE DÉTECTÉE - Vérifiez src/pages/")
    
    print("="*70)
    print("🌐 URL : http://127.0.0.1:8051/")
    print("⌨️  Ctrl+C pour arrêter")
    print("="*70 + "\n")

    app.run(debug=True, port=8051)
