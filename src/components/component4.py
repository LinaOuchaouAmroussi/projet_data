import plotly.express as px
from . import df, YEAR_COLUMN, SIZE_COLUMN

def create_size_evolution_plot():
    """
    Crée le graphique d'évolution des notes par taille d'entreprise
    avec animation temporelle
    """
    # Calculer les moyennes par année et taille
    means = (df.groupby([YEAR_COLUMN, SIZE_COLUMN])
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
    
    # Mise en page améliorée
    fig.update_layout(
        title_x=0.5,
        xaxis_title="Tranche d'effectifs",
        yaxis_title="Note moyenne",
        showlegend=True,
        template="plotly_white",
        height=600,
        width=1000,
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    
    # Améliorer l'apparence des lignes et points
    fig.update_traces(
        mode='lines+markers',
        line=dict(width=3),
        marker=dict(
            size=10,
            symbol='circle',
            line=dict(width=2, color='white')
        )
    )
    
    # Animation plus fluide
    fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000
    fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500
    
    return fig