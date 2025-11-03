import pandas as pd #on importe pandas pour la manipulation des données
import folium #on importe folium pour la création de cartes interactives
import geopandas #on importe geojson et geopandas pour la manipulation de données géospatiales


# on lit les données
data = pd.read_csv("data/cleaned/cleaneddata.csv")  # ton fichier nettoyé
france_dpt = geopandas.read_file("data/raw/departements.json")  # géodonnées

# On retire les lignes où la note n’est pas renseignée
data_filtered = data.dropna(subset=['note_index'])

# On calcule la moyenne par département
moyennes_dpt = data_filtered.groupby('département')['note_index'].mean().reset_index()

# On renomme pour correspondre au GeoJSON
moyennes_dpt.rename(columns={'département': 'nom', 'note_index': 'note_moyenne'}, inplace=True)

# Fusion entre les départements géographiques et les moyennes
geo_merged = france_dpt.merge(moyennes_dpt, on='nom', how='left')

# Création d'une carte centrée sur la France
carte = folium.Map(location=[46.5, 2], zoom_start=6, tiles='cartodb positron')

# Ajout du choroplèthe
folium.Choropleth(
    geo_data=geo_merged,
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

geojson_layer = folium.GeoJson(
    geo_merged,
    name="Détails des départements",
    style_function=lambda x: {
        "color": "transparent",   # pas de contour bleu
        "weight": 0
    },
    highlight_function=lambda x: {
        "weight": 2,
        "color": "black",
        "fillOpacity": 0.8
    },
    tooltip=folium.GeoJsonTooltip(
        fields=["nom", "note_moyenne"],
        aliases=["Département :", "Note moyenne :"],
        localize=True,
        sticky=True
    ),
    popup=folium.GeoJsonPopup(
        fields=["nom", "note_moyenne"],
        labels=False
    )
).add_to(carte)

carte.save("data/output/carte_egalite.html")
print("Carte générée : data/outputs/carte_egalite.html")