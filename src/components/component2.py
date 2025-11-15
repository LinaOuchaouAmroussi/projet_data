"""
Composant 2 : Notes moyennes par taille d'entreprise
"""
import plotly.express as px
from config import load_clean_df, NOTE_COLUMNS, SIZE_COLUMN

def create_size_distribution_plot():
    """Crée le graphique des notes moyennes par taille d'entreprise"""
    data = load_clean_df()
    # on calcule les moyennes par taille d'entreprise
    means = data.groupby(SIZE_COLUMN)[NOTE_COLUMNS].mean().reset_index()
    fig = px.bar(
        means,
        x=SIZE_COLUMN,
        y='note_index',
        title="Note Moyenne d'Égalité Professionnelle selon la Taille de l'Entreprise",
        labels={
            SIZE_COLUMN: "Taille de l'entreprise",
            'note_index': "Note moyenne globale"
        }
    )
    fig.update_layout(
        xaxis_title="Tranche d'effectifs",
        yaxis_title="Note moyenne",
        title_x=0.5,
        template="plotly_white",
        height=600,
        width=800,
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    # on modifie l'apparence des barres
    fig.update_traces(
        marker_color='#2874A6',
        marker_line_color='#1B4F72',
        marker_line_width=1.5,
        opacity=0.8
    )
    return fig
