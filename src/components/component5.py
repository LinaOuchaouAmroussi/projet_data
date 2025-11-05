import plotly.graph_objects as go
from src.components import df

def create_summary_stats():
    """Crée un résumé statistique des données"""
    return {
        "Note Moyenne Globale": df["note_index"].mean(),
        "Nombre d'Entreprises": len(df),
        "Années Couvertes": f"{df['année'].min()} - {df['année'].max()}",
        "Note Maximale": df["note_index"].max(),
        "Note Minimale": df["note_index"].min()
    }

def create_stats_table():
    """Crée une visualisation HTML des statistiques sous forme de tableau"""

    stats = {
        "Note Moyenne Globale": df["note_index"].mean(),
        "Nombre d'Entreprises": len(df),
        "Années Couvertes": f"{df['année'].min()} - {df['année'].max()}",
        "Note Maximale": df["note_index"].max(),
        "Note Minimale": df["note_index"].min()
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
            fill_color=[['#f2f2f2', 'white'] * 5],  # bandes zébrées élégantes
            align='center',
            font=dict(color='black', size=14),
            height=38
        )
    )])

    # ✅ Taille auto sans scroll
    fig.update_layout(
        height = 450,   # assez grand pour afficher toutes les lignes
        width = None,   # largeur automatique : prend toute la page
        margin=dict(t=40, b=30, l=20, r=20),
        paper_bgcolor='white'
    )

    return fig
