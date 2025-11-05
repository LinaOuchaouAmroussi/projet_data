from dash import Dash, html
from src.components.component_map import create_map  # <-- on importe la fonction

# --- Création de l’application Dash ---
app = Dash(__name__)
app.title = "Dashboard Égalité Professionnelle"

# --- Layout ---
app.layout = html.Div([
    html.H1(
        "🗺️ Carte de l'égalité professionnelle par département",
        style={'textAlign': 'center', 'color': '#003366'}
    ),

    html.Div(
        id='map-container',
        children=[
            html.Iframe(
                id='map',
                srcDoc=create_map(),   # on appelle la fonction importée
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
        "Cette carte affiche la note moyenne d’égalité professionnelle par département.",
        style={'textAlign': 'center', 'marginTop': '20px', 'fontSize': '18px'}
    )
])

# --- Lancement ---
if __name__ == "__main__":
    app.run(debug=True, port=8056)
