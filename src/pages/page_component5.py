# src/pages/page_component5.py

from dash import Dash, html, dcc
from src.components.component5 import create_stats_table  # ton composant existant

# Création de l'app Dash
app = Dash(__name__)

# Génération du tableau de statistiques à partir du composant
fig = create_stats_table()

# Définition de la page Dash
app.layout = html.Div([
    html.H1(
        "Statistiques Clés des Entreprises",
        style={"textAlign": "center", "color": "#0074D9"}
    ),
    html.P(
        "Cette page présente un résumé statistique des notes et des entreprises couvertes dans le dataset.",
        style={"textAlign": "center"}
    ),
    dcc.Graph(
        id="stats-table-graph",
        figure=fig
    )
])

# Lancement de l'application Dash
if __name__ == "__main__":
    app.run(debug=True, port=8055)
