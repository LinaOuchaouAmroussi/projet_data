
"""
Composant 1 : Distribution des notes
"""
import plotly.graph_objects as go
from plotly.subplots import make_subplots
"""from src.components import df, NOTE_COLUMNS"""
from config import df, NOTE_COLUMNS   # ✅ import direct du config global

def create_distribution_plot():
    """Creates the distribution plot for all notes"""
    valid_columns = [col for col in NOTE_COLUMNS if col in df.columns]
    
    # Create subplots avec les spécifications d'axes
    fig = make_subplots(
        rows=len(valid_columns), 
        cols=1,
        subplot_titles=[col.replace('_', ' ').title() for col in valid_columns],
        vertical_spacing=0.08,
        x_title="Note obtenue",
        y_title="Nombre d'entreprises"
    )
    
    for i, col in enumerate(valid_columns, 1):
        valid_data = df[col].dropna()
        if not valid_data.empty:
            fig.add_trace(
                go.Histogram(
                    x=valid_data,
                    name=col.replace('_', ' ').title(),
                    nbinsx=20,
                    marker_color='#5470C6'
                ),
                row=i, 
                col=1
            )
    
    # Mise à jour du layout global
    fig.update_layout(
        height=300*len(valid_columns),
        width=800,
        showlegend=False,
        title_text="Distribution des Notes d'Égalité Professionnelle par Catégorie",
        title_x=0.5,
        title_font=dict(
            size=24,
            family='Arial, sans-serif',
            color='#1f4788'
        ),
        font=dict(
            family='Arial, sans-serif',
            size=12,
            color='#2c3e50'
        )
    )
    
    # Mise à jour de TOUS les axes X et Y en une seule fois
    fig.update_xaxes(
        title_text="Note obtenue",
        title_font=dict(size=14, family='Arial, sans-serif', color='#2c3e50'),
        tickfont=dict(family='Arial, sans-serif', size=11)
    )
    
    fig.update_yaxes(
        title_text="Nombre d'entreprises",
        title_font=dict(size=14, family='Arial, sans-serif', color='#2c3e50'),
        tickfont=dict(family='Arial, sans-serif', size=11)
    )
    
    return fig