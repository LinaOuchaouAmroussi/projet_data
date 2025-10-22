import pandas as pd
import folium
import geopandas

# on charge nos données
data = pd.read_csv("data/cleaned/cleaneddata.csv")

# on garde les colonnes utiles pour notre map
data = data[["Raison Sociale", "Région", "Département", "Note Index"]]

# on nettoie
data = data[data["Note Index"] != "NC"] # a changer quand on aura nettoyer nos données == nan
data["Note Index"] = data["Note Index"].astype(float)

# on crée la moyenne par département
index_par_dep = data.groupby("Département")["Note Index"].mean().reset_index()

# on charge la carte des départements ####ATTENTION ON A PAS CA 
geo_df = geopandas.read_file("data/raw/departements.geojson")

# on nettoie les noms pour le merge
geo_df["nom"] = geo_df["nom"].str.lower()
index_par_dep["Département"] = index_par_dep["Département"].str.lower()

# on fusionne les deux dataframes
merged = geo_df.merge(index_par_dep, left_on="nom", right_on="Département")

# maintenant on crée la carte
coords = (46.603354, 1.888334) #on centre la carte sur la France (coordonnées du centre de la france)
map_france = folium.Map(location=coords, zoom_start=6) # on crée la map avce folium

folium.Choropleth(
    geo_data="data/raw/departements.geojson", #non mais 
    data=merged,
    columns=["nom", "Note Index"],
    key_on="feature.properties.nom",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Index égalité homme/femme moyen par département"
).add_to(map_france)

# on sauvegarde notre map
map_france.save("data/cleaned/map_index_egalite.html")
#print("Carte créée : data/cleaned/map_index_egalite.html")
