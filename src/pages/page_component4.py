# src/pages/page_component4.py

from dash import Dash, html, dcc
from src.components.component4 import create_size_evolution_plot  # ton composant existant

# Création de l'app Dash
app = Dash(__name__)

# Génération du graphique à partir du composant
fig = create_size_evolution_plot()

# Définition de la page Dash
app.layout = html.Div([
    html.H1(
        "Évolution des Notes par Taille d'Entreprise",
        style={"textAlign": "center", "color": "#0074D9"}
    ),
    html.P(
        "Cette page montre l'évolution annuelle de la note moyenne selon la taille de l'entreprise.",
        style={"textAlign": "center"}
    ),
    dcc.Graph(
        id="size-evolution-graph",
        figure=fig
    )
])

# Lancement de l'application Dash
if __name__ == "__main__":
    app.run(debug=True, port=8054)