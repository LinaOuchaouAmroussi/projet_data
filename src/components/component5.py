import plotly.graph_objects as go
from . import df

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
    stats = create_summary_stats()
    
    fig = go.Figure(data=[go.Table(
        header=dict(
            values=['Indicateur', 'Valeur'],
            fill_color='#2874A6',
            align='left',
            font=dict(color='white', size=16),
            height=40
        ),
        cells=dict(
            values=[
                list(stats.keys()),
                [f"{v:.2f}" if isinstance(v, (int, float)) else str(v) for v in stats.values()]
            ],
            fill_color='#EBF5FB',
            align='left',
            font=dict(color='black', size=14),
            height=35
        )
    )])
    
    fig.update_layout(
        title=dict(
            text="Tableau de Bord - Statistiques Clés",
            x=0.5,
            y=0.95,
            font=dict(size=24)
        ),
        width=800,
        height=400,
        margin=dict(t=100, b=50, l=50, r=50),
        paper_bgcolor='white'
    )
    
    return fig