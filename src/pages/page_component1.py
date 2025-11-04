# src/pages/page_component1.py

from dash import Dash, html, dcc
from src.components.component1 import create_distribution_plot  # ton composant existant

# Création de l'app Dash
app = Dash(__name__)

# On génère le graphique à partir du composant
fig = create_distribution_plot()

# Définition de la page Dash
app.layout = html.Div([
    html.H1(
        "Distribution des Notes d'Égalité Professionnelle",
        style={"textAlign": "center", "color": "#0074D9"}
    ),
    html.P(
        "Cette page montre la répartition des notes obtenues par les entreprises dans chaque catégorie.",
        style={"textAlign": "center"}
    ),
    dcc.Graph(
        id="distribution-graph",
        figure=fig
    )
])

# Lancement de l'application Dash
if __name__ == "__main__":
    app.run(debug=True, port=8051)
