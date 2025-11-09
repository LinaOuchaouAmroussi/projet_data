"""
Composant 3 : Évolution temporelle animée par région
"""
import plotly.express as px
"""from src.components import df, YEAR_COLUMN, REGION_COLUMN"""
from config import df, YEAR_COLUMN, REGION_COLUMN

def create_temporal_evolution_plot():
    """
    Crée le graphique d'évolution temporelle animé des notes
    avec coloration par région
    """
    fig = px.scatter(
        df, 
        x='note_index',
        y='note_ecart_rémunération',
        animation_frame=YEAR_COLUMN,
        color=REGION_COLUMN,
        title="Évolution des Notes d'Égalité Professionnelle par Année et Région",
        labels={
            'note_index': "Note globale",
            'note_ecart_rémunération': "Note écart de rémunération",
            REGION_COLUMN: "Région",
            YEAR_COLUMN: "Année"
        }
    )
    
    fig.update_layout(
        title_x=0.5,
        showlegend=True,
        template="plotly_white",
        height=600,
        width=1000,
        xaxis_title="Note globale d'égalité professionnelle",
        yaxis_title="Note sur l'écart de rémunération",
        legend_title="Régions",
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    
    # Améliorer l'apparence des points
    fig.update_traces(
        marker=dict(
            size=10,
            opacity=0.7,
            line=dict(width=1, color='white')
        )
    )
    
    # Ajouter des animations plus fluides
    fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000
    fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500
    
    return fig