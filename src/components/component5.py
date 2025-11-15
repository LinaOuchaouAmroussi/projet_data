import plotly.graph_objects as go
"""from src.components import df"""
from config import load_clean_df


def create_summary_stats():
    """Crée un résumé statistique des données"""
    data = load_clean_df()
    return {
        "Note Moyenne Globale": data["note_index"].mean(),
        "Nombre d'Entreprises": len(data),
        "Années Couvertes": f"{data['annee'].min()} - {data['annee'].max()}",
        "Note Maximale": data["note_index"].max(),
        "Note Minimale": data["note_index"].min()
    }

def create_stats_table():
    """Crée une visualisation HTML des statistiques sous forme de tableau"""
    data = load_clean_df()
    stats = {
        "Note Moyenne Globale": data["note_index"].mean(),
        "Nombre d'Entreprises": len(data),
        "Années Couvertes": f"{data['annee'].min()} - {data['annee'].max()}",
        "Note Maximale": data["note_index"].max(),
        "Note Minimale": data["note_index"].min()
    }

    fig = go.Figure(data=[go.Table(
        header=dict(
            values=['Indicateur', 'Valeur'],
            fill_color='#1f4788',
            align='center',
            font=dict(color='white', size=16),
            height=45
        ),
        cells=dict(
            values=[
                list(stats.keys()),
                [f"{v:.2f}" if isinstance(v, (int, float)) else str(v) for v in stats.values()]
            ],
            fill_color=[['#f2f2f2', 'white'] * 5], # alternance des couleurs
            align='center',
            font=dict(color='black', size=14),
            height=38
        )
    )])

    # taille auto
    fig.update_layout(
        height = 450,   # assez grand pour afficher toutes les lignes
        width = None,   # largeur automatique : prend toute la page
        margin=dict(t=40, b=30, l=20, r=20),
        paper_bgcolor='white'
    )

    return fig
