import plotly.graph_objects as go
from plotly.subplots import make_subplots
from components import df, NOTE_COLUMNS

def create_distribution_plot():
    """Crée le graphique de distribution des notes"""
    valid_columns = [col for col in NOTE_COLUMNS if col in df.columns]
    
    fig = make_subplots(
        rows=len(valid_columns), 
        cols=1,
        subplot_titles=[col.replace('_', ' ').title() for col in valid_columns]
    )
    
    for i, col in enumerate(valid_columns, 1):
        valid_data = df[col].dropna()
        if not valid_data.empty:
            fig.add_trace(
                go.Histogram(
                    x=valid_data,
                    name=col.replace('_', ' ').title(),
                    nbinsx=20
                ),
                row=i, 
                col=1
            )
    
    fig.update_layout(
        height=300*len(valid_columns),
        width=800,
        showlegend=False,
        title_text="Distribution des Notes d'Égalité Professionnelle par Catégorie",
        title_x=0.5,
        xaxis_title="Note obtenue",
        yaxis_title="Nombre d'entreprises"
    )
    
    return fig