# src/pages/page_component2.py

from dash import Dash, html, dcc
from src.components.component2 import create_size_distribution_plot  # ton composant existant

# Création de l'app Dash
app = Dash(__name__)

# Génération du graphique à partir du composant
fig = create_size_distribution_plot()

# Définition de la page Dash
app.layout = html.Div([
    html.H1(
        "Note Moyenne d'Égalité Professionnelle par Taille d'Entreprise",
        style={"textAlign": "center", "color": "#0074D9"}
    ),
    html.P(
        "Cette page montre la note moyenne globale par tranche de taille d'entreprise.",
        style={"textAlign": "center"}
    ),
    dcc.Graph(
        id="size-distribution-graph",
        figure=fig
    )
])

# Lancement de l'application Dash
if __name__ == "__main__":
    app.run(debug=True, port=8052)