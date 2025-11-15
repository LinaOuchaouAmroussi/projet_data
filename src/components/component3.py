"""
Composant 3 : Évolution temporelle des notes.
Crée un graphique animé par année et par région.
"""
import re
import numpy as np
import pandas as pd
import plotly.express as px
from config import load_clean_df, YEAR_COLUMN, REGION_COLUMN

def create_temporal_evolution_plot():
    """Crée le graphique animé de l'évolution des notes par année et région."""
    dff = load_clean_df().copy()
    # Nettoyage/tri des années
    def to_year(v):
        """Convertit une valeur en année entière ou NaN."""
        if pd.isna(v):
            return np.nan
        s = str(v).strip()
        # essaie conversion directe float->int (gère '2019.0', ' 2020 ')
        try:
            return int(float(s))
        except:
            digits = "".join(re.findall(r"\d+", s))
            return int(digits[:4]) if len(digits) >= 4 else np.nan

    dff[YEAR_COLUMN] = dff[YEAR_COLUMN].map(to_year).astype("Int64")
    dff = dff.dropna(subset=[YEAR_COLUMN])
    years = sorted(dff[YEAR_COLUMN].astype(int).unique().tolist())
    years_str = list(map(str, years))  # utile si Plotly recaste en str
    # borne fixe pour tous les axes
    pad_x = 1
    pad_y = 1
    x_min, x_max = float(dff["note_index"].min()) - pad_x, float(dff["note_index"].max()) + pad_x
    y_min, y_max = float(dff["note_ecart_remuneration"].min()) - pad_y, float(dff["note_ecart_remuneration"].max()) + pad_y
    entity_id_col = None
    fig = px.scatter(
        dff,
        x="note_index",
        y="note_ecart_remuneration",
        animation_frame=YEAR_COLUMN,
        animation_group=entity_id_col,
        color=REGION_COLUMN,
        category_orders={YEAR_COLUMN: years},
        title="Évolution des Notes d'Égalité Professionnelle par Année et Région",
        labels={
            "note_index": "Note globale",
            "note_ecart_rémunération": "Note écart de rémunération",
            REGION_COLUMN: "Région",
            YEAR_COLUMN: "Année",
        },
        template="plotly_white",
        height=600,
        width=1000,
        range_x=[x_min, x_max],
        range_y=[y_min, y_max],
    )
    #forcer l’ordre des frames et des steps
    # frames
    fig.frames = tuple(sorted(fig.frames, key=lambda f: int(f.name)))
    # steps du slider
    if fig.layout.sliders and len(fig.layout.sliders) > 0:
        slider = fig.layout.sliders[0]
        steps_sorted = sorted(slider["steps"], key=lambda s: int(s["label"]))
        # mise à jour immédiate pendant le drag
        for s in steps_sorted:
            # args = [frame_name, {options}]
            frame_name = s["label"]  # identique au label -> correspond au nom de frame
            s["args"] = [
                [str(frame_name)],  # cible la frame
                {
                    "frame": {"duration": 0, "redraw": True},
                    "mode": "immediate",
                    "transition": {"duration": 0},
                },
            ]
        slider["steps"] = steps_sorted
        slider["active"] = 0
        slider["transition"] = {"duration": 0}         # slider lui-même
        slider["currentvalue"] = {"prefix": "Année=", "visible": True}
    # boutons Play/Pause avec l'animation qui marche bien 
    if fig.layout.updatemenus and len(fig.layout.updatemenus) > 0:
        # Play: tu peux ajuster ces durées pour l’auto-play
        fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 700
        fig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 300
        # Stop: aucune transition
        fig.layout.updatemenus[0].buttons[1].args[1]["frame"]["duration"] = 0
        fig.layout.updatemenus[0].buttons[1].args[1]["transition"]["duration"] = 0
    # Style
    fig.update_layout(
        title_x=0.5,
        showlegend=True,
        xaxis_title="Note globale d'égalité professionnelle",
        yaxis_title="Note sur l'écart de rémunération",
        legend_title="Régions",
        plot_bgcolor="white",
        paper_bgcolor="white",
        transition={"duration": 0},  # interactions hors play
    )
    fig.update_traces(
        marker={"size": 10, "opacity": 0.7, "line": {"width": 1, "color": "white"}}
    )
    return fig
