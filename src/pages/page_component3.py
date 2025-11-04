# src/pages/page_component3.py

from dash import Dash, html, dcc
from src.components.component3 import create_temporal_evolution_plot  # ton composant existant

# Création de l'app Dash
app = Dash(__name__)

# Génération du graphique à partir du composant
fig = create_temporal_evolution_plot()

# Définition de la page Dash
app.layout = html.Div([
    html.H1(
        "Évolution Temporelle des Notes d'Égalité Professionnelle",
        style={"textAlign": "center", "color": "#0074D9"}
    ),
    html.P(
        "Cette page montre l'évolution annuelle des notes par région avec animation.",
        style={"textAlign": "center"}
    ),
    dcc.Graph(
        id="temporal-evolution-graph",
        figure=fig
    )
])

# Lancement de l'application Dash
if __name__ == "__main__":
    app.run(debug=True, port=8053)