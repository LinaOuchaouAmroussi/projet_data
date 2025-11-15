import plotly.express as px
"""from src.components import df, YEAR_COLUMN, SIZE_COLUMN"""
from config import load_clean_df, YEAR_COLUMN, SIZE_COLUMN

def create_size_evolution_plot():
    """Creates the animated evolution plot by company size"""
    # on calcule la moyenne des notes par taille et par année
    data = load_clean_df()
    means = (data.groupby([YEAR_COLUMN, SIZE_COLUMN])
            ['note_index'].mean().reset_index())
    
    fig = px.line(
        means, 
        x=SIZE_COLUMN,
        y='note_index',
        animation_frame=YEAR_COLUMN,
        title="Évolution de la Note Moyenne par Taille d'Entreprise",
        labels={
            SIZE_COLUMN: "Taille de l'entreprise",
            'note_index': "Note moyenne",
            YEAR_COLUMN: "Année"
        }
    )
    
    # on met a jour le layout
    fig.update_layout(
        height=600,
        width=800,
        showlegend=True,
        title_x=0.5,
        xaxis_title="Tranche d'effectifs",
        yaxis_title="Note moyenne",
        template="plotly_white"
    )
    
    # Ajout des marqueurs et amélioration de la visibilité des lignes
    fig.update_traces(
        mode='lines+markers',
        line=dict(width=3),
        marker=dict(
            size=10,
            symbol='circle',
            line=dict(width=2, color='white')
        )
    )
    
    # Animation
    fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000
    fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500
    
    return fig