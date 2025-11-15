# src/components/component_map.py
import pandas as pd
import geopandas
import folium
import io
import os
from config import RAW_DIR, df 



def create_map():
    """Crée la carte Folium et retourne le code HTML sous forme de texte.
    # Chargement des données
    data = pd.read_csv("data/cleaned/cleaneddata.csv")
    france_dpt = geopandas.read_file("data/raw/departements.json")"""

    #Crée la carte Folium et retourne le code HTML sous forme de texte
   # data = load_clean_df()
    france_dpt_path = os.path.join(RAW_DIR, "departements.json")
    france_dpt = geopandas.read_file(france_dpt_path)

    # Nettoyage
    data_filtered = df.dropna(subset=['note_index'])

    # Calcul des moyennes par département
    moyennes_dpt = (
        data_filtered.groupby('departement')['note_index']
        .mean()
        .reset_index()
        .rename(columns={'departement': 'nom', 'note_index': 'note_moyenne'})
    )

    # Fusion avec le GeoJSON
    geo_merged = france_dpt.merge(moyennes_dpt, on='nom', how='left')

    # S'assurer qu'il y a bien la colonne note_moyenne (même si toutes NaN)
    if 'note_moyenne' not in geo_merged.columns:
        geo_merged['note_moyenne'] = None

    # Création de la carte
    carte = folium.Map(location=[46.5, 2], zoom_start=6, tiles='cartodb positron')

    # folium.Choropleth accepte un geo_json string/dict — on lui donne le json
    geojson_str = geo_merged.to_json()

    folium.Choropleth(
        geo_data=geojson_str,
        name='Score égalité pro',
        data=geo_merged,
        columns=['nom', 'note_moyenne'],
        key_on='feature.properties.nom',
        fill_color='YlGnBu',
        nan_fill_color='lightgrey',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Note moyenne égalité professionnelle par département',
    ).add_to(carte)

    folium.GeoJson(
        geojson_str,
        name="Détails des départements",
        style_function=lambda x: {"color": "transparent", "weight": 0},
        highlight_function=lambda x: {"weight": 2, "color": "black", "fillOpacity": 0.8},
        tooltip=folium.GeoJsonTooltip(
            fields=["nom", "note_moyenne"],
            aliases=["Département :", "Note moyenne :"],
            localize=True,
            sticky=True
        )
    ).add_to(carte)

    # Sauvegarde dans un buffer BytesIO puis décodage en string
    map_buffer = io.BytesIO()
    carte.save(map_buffer, close_file=False)
    html_bytes = map_buffer.getvalue()
    html_str = html_bytes.decode('utf-8')
    return html_str
