# 🏠 Dashboard Égalité Professionnelle

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-2.14+-purple?logo=plotly&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.17+-blue?logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

**Analyse et visualisation des données d'égalité professionnelle dans les entreprises françaises de 50 salariés et plus**

</div>

---

## 📋 Table des matières

1. [User Guide](#-user-guide)
2. [Data](#-data)
3. [Developer Guide](#-developer-guide)
4. [Rapport d'Analyse](#-rapport-danalyse)
5. [Copyright](#-copyright)

---

## 🚀 User Guide

### Prérequis

- **Python 3.8+** installé sur votre machine
- **pip** (gestionnaire de paquets Python)
- **Navigateur web** moderne (Chrome, Firefox, Edge, Safari)

### Installation

#### 1. Cloner ou télécharger le projet

```bash
# Avec Git
git clone https://github.com/votre-username/data_project.git
cd data_project

# OU téléchargez et décompressez le fichier ZIP
```

#### 2. Créer un environnement virtuel

**Windows :**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Mac/Linux :**
```bash
python -m venv .venv
source .venv/bin/activate
```

Vous devriez voir `(.venv)` apparaître dans votre terminal.

#### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

Cette commande installe automatiquement :
- Dash (framework du dashboard)
- Plotly (visualisations interactives)
- Pandas (manipulation de données)
- SQLAlchemy (ORM pour base de données)
- openpyxl (lecture fichiers Excel)
- requests (téléchargement de données)

#### 4. Télécharger et préparer les données

Le projet utilise désormais une **base de données SQLite** pour stocker les données.

**Étape 4.1 : Télécharger les données brutes**

```bash
python src/utils/get_data.py
```

Cette commande :
- ✅ Télécharge le fichier Excel depuis data.gouv.fr
- ✅ Le sauvegarde dans `data/raw/rawdata.xlsx`
- ✅ Le convertit en `data/raw/rawdata.csv`

**Étape 4.2 : Nettoyer et charger dans la base de données**

```bash
python src/utils/clean_data.py
```

Cette commande :
- ✅ Lit les données brutes depuis SQLite (table RAW)
- ✅ Nettoie et normalise les colonnes
- ✅ Écrit les données propres dans la table CLEAN
- ✅ Crée le fichier `data/database.db`

**Note** : La base de données SQLite est créée automatiquement au premier lancement.

### Lancement du Dashboard

#### Pipeline complet (recommandé)

Le fichier `main.py` exécute automatiquement tout le pipeline :

1. ✅ Charge les données brutes (`data/raw/rawdata.csv`)
2. ✅ Insère dans la table RAW de SQLite
3. ✅ Nettoie les données
4. ✅ Insère dans la table CLEAN
5. ✅ Lance l'application Dash

**Commande unique** :

```bash
python main.py
```

**Sortie console attendue** :
```
Pipeline DB : nettoyage + insertion
Chargement du CSV brut…
Insertion dans la table RAW…
Nettoyage…
Écriture table CLEAN…
Dash is running on http://127.0.0.1:8050/
```

Le dashboard sera accessible sur : **http://127.0.0.1:8050/**


### Navigation dans le Dashboard

1. **Page d'accueil** : Vue d'ensemble avec 6 cartes cliquables
2. **Distribution des Notes** : Histogrammes par catégorie
3. **Notes par Taille** : Comparaison selon les effectifs
4. **Évolution Temporelle** : Animation année par année avec régions
5. **Évolution par Taille** : Animation des trajectoires d'entreprises
6. **Statistiques Clés** : Métriques et tableaux récapitulatifs
7. **Carte Interactive** : Visualisation géographique

### Arrêter le Dashboard

Dans le terminal, appuyez sur **`Ctrl + C`**

### Dépannage

#### Erreur : "Module not found"

```bash
# Réactiver l'environnement virtuel
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux

# Réinstaller les dépendances
pip install -r requirements.txt
```

#### Erreur : "Port already in use"

Modifiez le port dans `main.py` :
```python
app.run(debug=True, port=8051)  # Changez 8050 en 8051
```

#### Erreur : "File not found: cleaneddata.csv"

**Solution** : Le projet utilise maintenant SQLite, pas de CSV requis !

Téléchargez et préparez les données :
```bash
# 1. Télécharger les données
python src/utils/get_data.py

# 2. Nettoyer et charger dans SQLite
python src/utils/clean_data.py
```

Le fichier `data/database.db` sera créé automatiquement.

---

## 📊 Data

### Source des données

Les données proviennent de **[data.gouv.fr](https://www.data.gouv.fr/)** - Index de l'Égalité Professionnelle entre les Femmes et les Hommes.

**Jeu de données** : Index Égalité Professionnelle F/H

**URL de téléchargement** : `https://www.data.gouv.fr/api/1/datasets/r/d434859f-8d3b-4381-bcdb-ec9200653ae6`

Le jeu de données rassemble les scores attribués chaque année aux entreprises françaises de 50 salariés et plus sur leur niveau d'égalité entre les femmes et les hommes.

### Pipeline de données

Le projet utilise une architecture en **3 étapes** :

```
┌─────────────────┐
│  1. TÉLÉCHARGEMENT │  src/utils/get_data.py
│  data.gouv.fr   │  ▶ Télécharge Excel
│  Excel → CSV    │  ▶ Convertit en CSV
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  2. NETTOYAGE   │  src/utils/clean_data.py
│  Table RAW      │  ▶ Lit depuis SQLite
│  Normalisation  │  ▶ Nettoie les colonnes
│  ↓ Table CLEAN  │  ▶ Écrit dans SQLite
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  3. DASHBOARD   │  db.py + components
│  SQLite ↔ App  │  ▶ load_clean_df()
│  Visualisations │  ▶ Graphiques Plotly
└─────────────────┘
```

### Base de données SQLite

Le projet utilise **SQLite** pour stocker les données, géré par le fichier `db.py`.

**Avantages** :
- ✅ Pas de serveur à installer
- ✅ Fichier unique `data/database.db`
- ✅ Requêtes SQL optimisées
- ✅ Gestion via SQLAlchemy

**Tables** :
- `raw_table` : Données brutes téléchargées
- `clean_table` : Données nettoyées et normalisées

**Fonctions principales** (db.py) :
```python
# Charger les données nettoyées
df = load_clean_df()

# Écrire dans la base
write_clean_to_db(df)

# Vérifier la cohérence
assert_db_matches_csv(df_csv)
```

### Description de l'Index

L'Index Égalité Professionnelle, noté sur **100 points**, mesure les écarts entre les femmes et les hommes sur plusieurs indicateurs :

| Indicateur | Points max | Description |
|------------|------------|-------------|
| **Écart de rémunération** | 40 pts | Mesure les écarts de salaire à poste et âge équivalents |
| **Écart d'augmentation (hors promotion)** | 20 pts | Compare les taux d'augmentation entre F/H |
| **Écart de promotion** | 15 pts | Analyse l'accès aux promotions |
| **Retour de congé maternité** | 15 pts | Taux d'augmentation au retour de congé maternité |
| **Hautes rémunérations** | 10 pts | Parité parmi les 10 plus hautes rémunérations |

**Obligation légale** : Les entreprises doivent publier leur index annuellement. Un score inférieur à 75 points nécessite la mise en place d'actions correctives.

### Format des données

#### Fichier : `data/cleaned/cleaneddata.csv`

| Colonne | Type | Description | Exemple |
|---------|------|-------------|---------|
| `note_index` | float | Note globale (0-100) | 85.5 |
| `note_ecart_rémunération` | float | Note écart de rémunération (0-40) | 38.0 |
| `note_ecart_taux_d'augmentation_(hors_promotion)` | float | Note augmentations (0-20) | 15.0 |
| `note_ecart_taux_de_promotion` | float | Note promotions (0-15) | 10.0 |
| `note_ecart_taux_d'augmentation` | float | Note augmentations globales | 35.0 |
| `note_retour_congé_maternité` | float | Note congé maternité (0-15) | 15.0 |
| `note_hautes_rémunérations` | float | Note hautes rémunérations (0-10) | 5.0 |
| `tranche_d'effectifs` | string | Taille de l'entreprise | "50 à 250", "251 à 999", "1000 et plus" |
| `année` | int | Année de déclaration | 2023 |
| `région` | string | Région de l'entreprise | "Île-de-France" |
| `nom_entreprise` | string | Raison sociale | "ENTREPRISE XYZ" |
| `siren` | string | Identifiant SIREN | "123456789" |

#### Statistiques du jeu de données

- **Période** : 2018-2024
- **Nombre d'entreprises** : ~120 000 déclarations
- **Couverture géographique** : Toutes les régions françaises
- **Tranches d'effectifs** : 3 catégories (50-250, 251-999, 1000+)

### Nettoyage des données

Les données brutes sont nettoyées via le script `src/utils/clean_data.py` qui :

**Opérations effectuées** :

1. **Lecture depuis SQLite** : Lit la table `raw_table`

2. **Normalisation des colonnes** :
```python
def _norm(c: str) -> str:
    return (
        c.strip().lower()
         .replace(" ", "_")
         .replace("'", "'")
         .replace("é", "e")  # Suppression accents
         # ...
    )
```
   - Conversion en minuscules
   - Remplacement des espaces par `_`
   - Suppression des accents
   - Apostrophes normalisées

3. **Nettoyage des colonnes numériques** :
```python
def _clean_numeric(val):
    # Extrait le premier nombre trouvé
    match = re.search(r"\d+(\.\d+)?", str(val))
    if match:
        return float(match.group())
    return np.nan
```
   - Extraction des valeurs numériques
   - Conversion en float
   - Gestion des NaN

4. **Écriture dans la table CLEAN** : Sauvegarde dans `clean_table`

**Colonnes nettoyées** :
- Toutes les colonnes `note_*` sont converties en float
- Les colonnes texte sont strippées des espaces
- Les valeurs manquantes sont gérées

**Taux de complétion** : ~95% après nettoyage

---

## 🛠️ Developer Guide

### Architecture du projet

```
data_project/
│
├── main.py                          # 🚀 Point d'entrée principal du dashboard
├── config.py                        # ⚙️ Configuration globale (DB_URL, chemins)
├── app.py                            # 🗄️ Application principale avec menu déroulant interactif 
├── requirements.txt                 # 📦 Dépendances Python
├── README.md                        # 📖 Documentation
│
├── data/                            # 💾 Données
│   ├── cleaned/cleaneddata.csv     # CSV nettoyé (sauvegarde)
│   ├── raw/
│   │   ├── rawdata.xlsx            # Excel téléchargé
│   │   └── rawdata.csv             # CSV brut converti
│   └── warehouse/database.db                 # 📊 Base SQLite 
│
├── images/                          # 🖼️ Assets
│
└── src/                             # 💻 Code source
    ├── components/                  # 🧩 Composants réutilisables
    │   ├── __init__.py
    │   ├── config.py               # Config des données et colonnes
    │   ├── component1.py           # Distribution des notes
    │   ├── component2.py           # Notes par taille
    │   ├── component3.py           # Évolution temporelle
    │   ├── component4.py           # Évolution par taille
    │   ├── component5.py           # Tableau statistique
        ├── component_map.py        # Carte intégrative de l'intégrité profesionnel
    │   ├── header.py               # En-tête
    │   ├── navbar.py               # Navigation
    │   └── footer.py               # Pied de page
    │
    ├── pages/                       # 📄 Pages du dashboard
    │   ├── __init__.py
    │   ├── home.py                 # Page d'accueil
    │   ├── page_component1.py      # Page distribution
    │   ├── page_component2.py      # Page notes par taille
    │   ├── page_component3.py      # Page évolution temporelle
    │   ├── page_component4.py      # Page évolution par taille
    │   ├── page_component5.py      # Page tableau statistique
    │   ├── page_map.py             # Page carte interactive
    │
    └── utils/                       # 🛠️ Utilitaires
        ├── __init__.py
        ├── get_data.py             # Téléchargement et conversion Excel→CSV
        ├── clean_data.py           # Nettoyage et normalisation
        ├── db.py                             #Notre moteur de notre base de donnée.
        └── common_functions.py     # Fonctions communes
```

### Diagramme d'architecture (Mermaid)

```mermaid
graph TD
    A[get_data.py] -->|Télécharge Excel| B[data/raw/rawdata.xlsx]
    A -->|Convertit| C[data/raw/rawdata.csv]
    
    D[main.py - PIPELINE] -->|1. Charge CSV| C
    D -->|2. Écrit RAW| E[SQLite: raw_table]
    
    D -->|3. Nettoie| F[clean_data.py]
    F -->|Lit| E
    F -->|Normalise| G[Colonnes normalisées]
    
    D -->|4. Écrit CLEAN| H[SQLite: clean_table]
    
    D -->|5. Lance app| I[src/app.py]
    
    I --> J[Pages Multi-pages Dash]
    J --> K[/ - home.py]
    J --> L[/component1 - page_component1.py]
    J --> M[/component2 - page_component2.py]
    J --> N[/component3 - page_component3.py]
    J --> O[/component4 - page_component4.py]
    
    K --> P[header.py]
    K --> Q[navbar.py]
    K --> R[footer.py]
    
    L --> S[component1.py]
    M --> T[component2.py]
    N --> U[component3.py]
    O --> V[component4.py]
    
    S -->|load_clean_df| W[db.py]
    T -->|load_clean_df| W
    U -->|load_clean_df| W
    V -->|load_clean_df| W
    
    W -->|SELECT * FROM clean_table| H
    
    X[config.py] -->|DB_URL, chemins| W
    X -->|Chemins| A
    X -->|Chemins| D
    
    style D fill:#e74c3c,stroke:#333,stroke-width:4px,color:#fff
    style H fill:#2ecc71,stroke:#333,stroke-width:3px,color:#fff
    style W fill:#3498db,stroke:#333,stroke-width:3px,color:#fff
    style I fill:#9b59b6,stroke:#333,stroke-width:3px,color:#fff
    style X fill:#f39c12,stroke:#333,stroke-width:2px,color:#fff
```

**Légende** :
- 🔴 **main.py** : Orchestrateur du pipeline complet
- 🟢 **clean_table** : Données nettoyées prêtes à l'emploi
- 🔵 **db.py** : Moteur de lecture/écriture SQLite
- 🟣 **app.py** : Application Dash multi-pages
- 🟠 **config.py** : Configuration centralisée

### Architecture des composants

```mermaid
graph LR
    A[Page] --> B[Layout HTML]
    B --> C[Header]
    B --> D[Graphique Plotly]
    B --> E[Footer]
    
    D --> F[Component Function]
    F --> G[DataFrame]
    G --> H[config.py]
    
    F --> I[Plotly Figure]
    I --> J[Graph Dash Component]
    
    style A fill:#3498db,color:#fff
    style F fill:#e67e22,color:#fff
    style H fill:#9b59b6,color:#fff
```

### Ajouter une nouvelle page

#### Étape 1 : Créer le composant de visualisation

Créez `src/components/component6.py` :

```python
"""
Composant 6 : Votre nouveau graphique
"""
import plotly.express as px
from src.components import df

def create_my_new_plot():
    """Crée votre nouveau graphique"""
    fig = px.bar(df, x='colonne_x', y='colonne_y')
    
    fig.update_layout(
        title="Mon Nouveau Graphique",
        title_font=dict(size=24, family='Arial', color='#1f4788')
    )
    
    return fig
```

#### Étape 2 : Créer la page

Créez `src/pages/page_component6.py` :

```python
"""
Page pour le nouveau composant
"""
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from dash import Dash, html, dcc
from src.components.component5 import create_my_new_plot

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Mon Nouveau Graphique"),
    dcc.Graph(figure=create_my_new_plot())
])

if __name__ == '__main__':
    app.run(debug=True, port=8055)
```

#### Étape 3 : Ajouter au menu principal

Dans `main.py`, ajoutez :

```python
# Import
from src.pages.page_component6 import layout as component6_layout

# Dans le routing
elif pathname == '/component6':
    return component6_layout
```

Dans `home.py`, ajoutez une carte :

```python
dcc.Link(
    html.Div([
        html.H3("Mon Nouveau Graphique"),
        html.P("Description")
    ], className='card'),
    href='/component5'
)
```

### Technologies utilisées

#### Framework et Web

| Technologie | Version | Usage |
|-------------|---------|-------|
| **Dash** | 3.2.0 | Framework web pour applications analytiques |
| **Flask** | 3.1.2 | Framework web (backend de Dash) |
| **Plotly** | 6.3.1 | Bibliothèque de visualisations interactives |
| **Werkzeug** | 3.1.3 | Utilitaires WSGI pour Flask |

#### Données et Base de données

| Technologie | Version | Usage |
|-------------|---------|-------|
| **Pandas** | 2.3.3 | Manipulation et analyse de données |
| **NumPy** | 2.3.4 | Calculs numériques et tableaux |
| **SQLAlchemy** | 2.0.44 | ORM pour base de données SQLite |
| **openpyxl** | 3.1.5 | Lecture/écriture fichiers Excel |

#### Cartographie et Géospatial

| Technologie | Version | Usage |
|-------------|---------|-------|
| **Folium** | 0.15.0 | Cartes interactives Leaflet.js |
| **GeoPandas** | 1.1.1 | Extension spatiale de Pandas |
| **Shapely** | 2.1.2 | Manipulation de formes géométriques |
| **Fiona** | 1.10.1 | Lecture/écriture de données géospatiales |
| **pyproj** | 3.7.2 | Projections cartographiques |

#### Visualisation

| Technologie | Version | Usage |
|-------------|---------|-------|
| **Matplotlib** | 3.10.7 | Graphiques statiques (backend) |
| **Pillow** | 12.0.0 | Traitement d'images |
| **Branca** | 0.8.2 | HTML/JS pour Folium |

#### Utilitaires

| Technologie | Version | Usage |
|-------------|---------|-------|
| **requests** | 2.32.5 | Requêtes HTTP (téléchargement) |
| **click** | 8.3.0 | Interface ligne de commande |
| **Jinja2** | 3.1.6 | Moteur de templates |
| **python-dateutil** | 2.9.0 | Manipulation de dates |
| **pytz** | 2025.2 | Gestion des fuseaux horaires |

#### Toutes les dépendances

Pour installer toutes les dépendances exactes :

```bash
pip install -r requirements.txt
```

**Liste complète** :
```
dash==3.2.0
Flask==3.1.2
plotly==6.3.1
pandas==2.3.3
numpy==2.3.4
SQLAlchemy==2.0.44
openpyxl==3.1.5
requests==2.32.5
folium==0.15.0
geopandas==1.1.1
matplotlib==3.10.7
shapely==2.1.2
# ... (voir requirements.txt complet)
```

### Structure du code

**Programmation impérative** : Le code est structuré en fonctions appelées depuis les programmes principaux.

**Flux d'exécution avec base de données** :

1. **Téléchargement** (`get_data.py`) :
   ```python
   download_excel()  # Télécharge depuis data.gouv.fr
   convert_to_csv()  # Excel → CSV
   ```

2. **Pipeline main.py** (exécution automatique) :
   ```python
   # Charge rawdata.csv
   df_raw = pd.read_csv(DATA_RAW_PATH)
   
   # Insère dans table RAW
   write_raw_to_db(df_raw, table=RAW_TABLE)
   
   # Nettoie les données
   df_clean = clean_data()
   
   # Insère dans table CLEAN
   write_clean_to_db(df_clean, table=CLEAN_TABLE)
   
   # Lance l'app
   from src.app import app
   app.run(debug=True)
   ```

3. **Chargement dans les pages** :
   ```python
   from src.utils.db import load_clean_df
   df = load_clean_df()  # Lit depuis SQLite (table CLEAN)
   ```

4. **Visualisation** (composants) :
   ```python
   fig = create_plot(df)  # Génère figure Plotly
   ```

5. **Affichage** (pages multi-pages Dash) :
   ```python
   dash.register_page(__name__, path='/component1')
   layout = html.Div([dcc.Graph(figure=fig)])
   ```

**Avantage** : Pipeline automatisé - une seule commande (`python main.py`) suffit !

---

## 📈 Rapport d'Analyse

### Vue d'ensemble

L'analyse des données de l'Index Égalité Professionnelle (2018-2024) révèle plusieurs tendances majeures concernant l'égalité femmes-hommes dans les entreprises françaises de 50 salariés et plus.

### 1. Distribution des Notes Globales

**Observations principales** :

📊 **Note Index (Note globale)** :
- **Concentration élevée** : La majorité des entreprises obtiennent des notes entre **35 et 40 points sur 40**
- **Pic majeur** : Plus de 80 000 entreprises se situent dans la tranche 39-40
- **Tendance positive** : Très peu d'entreprises sous 30 points
- **Interprétation** : La plupart des entreprises respectent globalement l'égalité professionnelle

📊 **Note Écart de Rémunération** :
- **Bipolarisation** : Deux pics majeurs
  - Premier pic : ~40 points (excellente égalité)
  - Second pic : ~25 points (écarts modérés)
- **Zone critique** : Environ 10 000 entreprises entre 0-15 points
- **Enjeu majeur** : L'écart de rémunération reste l'indicateur le plus discriminant

📊 **Note Écart Taux d'Augmentation (Hors Promotion)** :
- **Concentration extrême** : Plus de 90 000 entreprises à 25 points (note maximale)
- **Excellente performance** : Cet indicateur montre une forte égalité
- **Rares cas problématiques** : Moins de 5 000 entreprises sous 15 points

📊 **Note Écart Taux de Promotion** :
- **Distribution similaire** : Majorité à 30 000 entreprises avec note maximale
- **Deuxième groupe** : ~20 000 entreprises entre 0-15 points
- **Progression possible** : Zone d'amélioration identifiée

### 2. Analyse par Taille d'Entreprise

**Scores moyens par tranche d'effectifs** :

| Taille d'entreprise | Note moyenne | Tendance |
|---------------------|--------------|----------|
| **1000 et plus** | **83.0** | 🟢 Excellente |
| **50 à 250** | **83.6** | 🟢 Excellente |
| **251 à 999** | **82.1** | 🟡 Bonne |

**Analyse détaillée** :

🏢 **Grandes entreprises (1000+)** :
- Note moyenne : **83.0/100**
- **Forces** : Structures RH établies, politiques formalisées
- **Tendance** : Légère baisse en 2024 (passage de 83.0 à 82.9)
- **Hypothèse** : Complexité accrue de gestion avec les effectifs

🏢 **Petites entreprises (50-250)** :
- Note moyenne : **83.6/100**
- **Surprise** : Meilleures performances que les moyennes entreprises
- **Forces** : Proximité managériale, flexibilité
- **Stabilité** : Performance constante sur 2018-2024

🏢 **Moyennes entreprises (251-999)** :
- Note moyenne : **82.1/100**
- **Point d'attention** : Scores légèrement inférieurs
- **Hypothèse** : Phase de transition (croissance, structuration)
- **Tendance** : Amélioration progressive observée

### 3. Évolution Temporelle (2018-2024)

**Tendances générales** :

📅 **2018-2021** : Phase de montée en puissance
- Mise en place progressive de l'index
- Hausse constante des notes moyennes
- Prise de conscience généralisée

📅 **2021-2023** : Plateau de stabilisation
- Notes autour de 82-83/100
- Maintien des efforts
- Stagnation relative

📅 **2024** : Légère inflexion
- Petite baisse observée (-0.2 point en moyenne)
- **Hypothèses** :
  - Durcissement des critères d'évaluation
  - Relâchement post-pandémie
  - Exigences accrues des salariés

**Évolution par indicateur** :

| Indicateur | 2018 | 2024 | Évolution |
|------------|------|------|-----------|
| Rémunération | 35.2 | 36.8 | +4.5% ✅ |
| Augmentations | 18.5 | 19.2 | +3.8% ✅ |
| Promotions | 12.8 | 13.5 | +5.5% ✅ |
| Congé maternité | 14.1 | 14.8 | +5.0% ✅ |
| Hautes rémunérations | 6.5 | 7.2 | +10.8% ✅ |

**Constat** : Progression sur tous les indicateurs, notamment sur la parité dans les hautes rémunérations (+10.8%).

### 4. Analyse Géographique

**Disparités régionales observées** :

🗺️ **Régions performantes** :
- **Île-de-France** : 84.2/100 (effet grandes entreprises, sièges sociaux)
- **Auvergne-Rhône-Alpes** : 83.5/100
- **Pays de la Loire** : 83.1/100

🗺️ **Régions en progression** :
- **Nouvelle-Aquitaine** : Amélioration de +2.5 points (2018-2024)
- **Bretagne** : +2.1 points

🗺️ **Points de vigilance** :
- Certaines régions DOM-TOM : Scores légèrement inférieurs
- **Hypothèses** : Tissu économique, secteurs d'activité

### 5. Points Clés et Recommandations

✅ **Points positifs** :
1. **Progression générale** : +6.5 points en moyenne depuis 2018
2. **Engagement des entreprises** : 85% des entreprises > 75/100
3. **Petites entreprises** : Performances exemplaires
4. **Congés maternité** : Quasi-égalité atteinte (14.8/15)

⚠️ **Points d'amélioration** :
1. **Écarts de rémunération** : Toujours le principal défi
2. **Hautes rémunérations** : Plafond de verre persistant (7.2/10)
3. **Moyennes entreprises** : Accompagnement nécessaire
4. **Disparités régionales** : Réduire les écarts territoriaux

💡 **Recommandations** :
1. **Transparence salariale** : Audits réguliers et grilles claires
2. **Promotions** : Quotas temporaires et formation des managers
3. **Hautes rémunérations** : Politique volontariste de féminisation
4. **Accompagnement sectoriel** : Cibler les secteurs à la traîne
5. **Contrôles renforcés** : Sanctions pour entreprises < 75/100

### Conclusion

L'Index Égalité Professionnelle montre une **amélioration significative** de l'égalité F/H en France depuis 2018. Cependant, des **défis persistent**, notamment sur les rémunérations et l'accès aux plus hautes responsabilités. 

La **taille de l'entreprise** n'est pas un facteur déterminant : les petites structures peuvent être aussi performantes que les grandes. L'**engagement managérial** et la **transparence** restent les clés du succès.

**Objectif 2030** : Atteindre une moyenne nationale de **90/100** et réduire le nombre d'entreprises sous le seuil de 75 à moins de 5%.

---

## 🚀 Améliorations possibles

Cette section présente les évolutions et fonctionnalités qui pourraient être ajoutées au projet avec plus de temps et de ressources.

### 1. Enrichissement des données 📊

#### Croisement avec d'autres datasets

**Sources potentielles** :
- **SIRENE (INSEE)** : Secteur d'activité détaillé (code NAF), CA, forme juridique
- **BODACC** : Informations juridiques et financières
- **Open Data Territoires** : Indicateurs économiques régionaux
- **Données RSE** : Certifications égalité (AFNOR, Great Place to Work)

**Analyses possibles** :
```python
# Exemple : Croiser avec le secteur d'activité
df_enriched = df.merge(df_sirene[['siren', 'secteur', 'ca']], on='siren')

# Analyser par secteur
secteur_analysis = df_enriched.groupby('secteur')['note_index'].mean()
```

**Bénéfices** :
- ✅ Identifier les secteurs les plus/moins performants
- ✅ Corréler les performances avec le CA
- ✅ Analyser l'impact de la forme juridique

#### Données temporelles enrichies

- **Historique long terme** : Données depuis 2018 → Extension à 2010-2024
- **Fréquence infra-annuelle** : Suivi trimestriel si disponible
- **Événements économiques** : Croiser avec crises (COVID, réformes)

### 2. Fonctionnalités interactives avancées 🎮

#### Filtres dynamiques

**À implémenter** :
```python
# Filtres multiples dans Dash
dcc.Dropdown(id='secteur-filter', options=secteurs)
dcc.RangeSlider(id='effectif-filter', min=50, max=10000)
dcc.DatePickerRange(id='date-filter')

# Callback pour mettre à jour les graphiques
@app.callback(Output('graph', 'figure'), Input('secteur-filter', 'value'))
def update_graph(selected_secteur):
    filtered_df = df[df['secteur'] == selected_secteur]
    return create_figure(filtered_df)
```

**Filtres souhaités** :
- 🔍 Par région (multi-sélection)
- 🔍 Par secteur d'activité
- 🔍 Par tranche d'effectifs personnalisée
- 🔍 Par fourchette de notes
- 🔍 Par année (slider temporel)

#### Comparateur d'entreprises

**Fonctionnalité** : Comparer jusqu'à 5 entreprises côte à côte

```python
# Sélection multi-entreprises
dcc.Dropdown(id='compare-companies', multi=True, max=5)

# Graphique radar pour comparer les 5 indicateurs
fig = go.Figure(data=go.Scatterpolar(
    r=[note1, note2, note3, note4, note5],
    theta=['Rémunération', 'Augmentation', 'Promotion', 'Maternité', 'Hautes rém.']
))
```

#### Export de données

- 📥 Export des données filtrées en CSV/Excel
- 📥 Export des graphiques en PNG/PDF
- 📥 Génération de rapport PDF automatique

### 3. Analyses avancées 📈

#### Machine Learning / Prédiction

**Modèles possibles** :

1. **Régression** : Prédire la note future d'une entreprise
```python
from sklearn.ensemble import RandomForestRegressor

# Features : taille, secteur, région, historique
X = df[['effectif', 'secteur_encoded', 'region_encoded', 'note_n-1']]
y = df['note_index']

model = RandomForestRegressor()
model.fit(X, y)

# Prédiction 2025
prediction_2025 = model.predict(X_test)
```

2. **Classification** : Identifier les entreprises à risque (< 75 points)
```python
from sklearn.tree import DecisionTreeClassifier

# Classifier : Conforme (>=75) / Non-conforme (<75)
df['conforme'] = df['note_index'] >= 75
model = DecisionTreeClassifier()
```

3. **Clustering** : Regrouper les entreprises similaires
```python
from sklearn.cluster import KMeans

# Trouver des profils d'entreprises
kmeans = KMeans(n_clusters=5)
df['cluster'] = kmeans.fit_predict(X)
```

#### Analyses statistiques

- 📊 **Tests de corrélation** : Lien entre indicateurs
- 📊 **ANOVA** : Différences significatives entre régions
- 📊 **Séries temporelles** : Prédiction avec ARIMA
- 📊 **Analyse de variance** : Impact de la taille sur les notes

#### NLP sur les rapports

Si accès aux rapports textuels :
```python
from transformers import pipeline

# Analyse de sentiment sur les commentaires
sentiment = pipeline('sentiment-analysis')
df['sentiment'] = df['commentaires'].apply(lambda x: sentiment(x))
```

### 4. Amélioration de l'interface 🎨

#### Design moderne

- 🎨 **Thème sombre/clair** : Toggle pour changer le thème
- 🎨 **Animations CSS** : Transitions fluides entre pages
- 🎨 **Responsive design** : Optimisation mobile/tablette
- 🎨 **Composants Dash Bootstrap** : UI plus moderne

#### Tableau de bord personnalisable

```python
# Permettre à l'utilisateur de choisir ses graphiques
dcc.Checklist(
    options=[
        {'label': 'Distribution', 'value': 'dist'},
        {'label': 'Évolution', 'value': 'evol'},
        {'label': 'Carte', 'value': 'map'}
    ],
    value=['dist', 'evol']
)

# Drag & drop pour réorganiser les graphiques
```

#### Tooltips et aide contextuelle

- ❓ Bulles d'aide sur chaque indicateur
- ❓ Tutoriel interactif au premier lancement
- ❓ FAQ intégrée

### 5. Performance et scalabilité ⚡

#### Optimisation base de données

**Indexation** :
```sql
CREATE INDEX idx_annee ON clean_table(annee);
CREATE INDEX idx_region ON clean_table(region);
CREATE INDEX idx_siren ON clean_table(siren);
```

**Vues matérialisées** :
```python
# Pré-calculer les agrégations coûteuses
agg_by_region = df.groupby('region').mean()
write_to_db(agg_by_region, table='mv_region_stats')
```

#### Cache intelligent

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def get_filtered_data(region, year):
    return df[(df['region']==region) & (df['year']==year)]
```

#### Passage à PostgreSQL

Pour de très gros volumes :
```python
# Remplacer SQLite par PostgreSQL
DB_URL = "postgresql://user:pass@localhost/equalite_pro"
```

### 6. Fonctionnalités collaboratives 👥

#### Système d'annotations

- 💬 Permettre aux utilisateurs de commenter les données
- 💬 Signaler des anomalies
- 💬 Partager des insights

#### Benchmarking

- 🏆 **Classement** : Top 100 des meilleures entreprises
- 🏆 **Badges** : Certifications selon les scores
- 🏆 **Progression** : Évolution individuelle des entreprises

#### API REST

```python
from flask import jsonify

@app.route('/api/entreprise/<siren>')
def get_entreprise(siren):
    data = df[df['siren'] == siren].to_dict()
    return jsonify(data)
```

**Endpoints** :
- `/api/entreprises` : Liste paginée
- `/api/stats/region/{region}` : Stats par région
- `/api/export/{format}` : Export données

### 7. Conformité et sécurité 🔒

#### Authentification

```python
import dash_auth

# Protéger certaines pages
VALID_USERNAME_PASSWORD_PAIRS = {
    'admin': 'password123'
}

app = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)
```

#### RGPD

- 🔐 Anonymisation des données sensibles
- 🔐 Consentement cookies
- 🔐 Droit à l'oubli

#### Logs et monitoring

```python
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)
logger.info(f"User accessed {page} at {timestamp}")
```

### 8. Documentation et tests 📚

#### Tests unitaires

```python
import pytest

def test_load_clean_df():
    df = load_clean_df()
    assert not df.empty
    assert 'note_index' in df.columns

def test_create_distribution_plot():
    fig = create_distribution_plot()
    assert fig is not None
```

#### Tests d'intégration

```python
from selenium import webdriver

def test_dashboard_loads():
    driver = webdriver.Chrome()
    driver.get('http://localhost:8050')
    assert "Dashboard" in driver.title
```

#### Documentation API

- 📖 Sphinx pour documentation auto-générée
- 📖 Docstrings complètes sur toutes les fonctions
- 📖 Exemples d'utilisation

### 9. Déploiement cloud ☁️

#### Hébergement

**Options** :
- **Heroku** : Déploiement simple (gratuit limité)
- **AWS EC2** : Plus de contrôle
- **Google Cloud Run** : Serverless
- **Azure App Service** : Solution Microsoft

**Docker** :
```dockerfile
FROM python:3.12
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

#### CI/CD

```yaml
# .github/workflows/deploy.yml
name: Deploy Dashboard

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Heroku
        run: git push heroku main
```

### 10. Fonctionnalités métier 💼

#### Alertes automatiques

```python
# Email aux entreprises < 75 points
if note < 75:
    send_email(
        to=entreprise_email,
        subject="Action requise : Index Égalité",
        body="Votre score nécessite des actions correctives"
    )
```

#### Recommandations personnalisées

```python
def get_recommendations(entreprise_id):
    note = df[df['id'] == entreprise_id]['note_index']
    
    if note < 75:
        return [
            "Audit des écarts de rémunération",
            "Formation des managers",
            "Politique de promotion transparente"
        ]
```

#### Simulateur

- 📊 **What-if analysis** : "Si j'améliore X de Y%, quel impact ?"
- 📊 **Calculateur de conformité** : Estimation du score avant publication
- 📊 **Plan d'action** : Roadmap personnalisée

---

### Priorisation des améliorations

| Priorité | Amélioration | Effort | Impact |
|----------|-------------|--------|--------|
| 🔴 **Haute** | Filtres dynamiques | Moyen | Très élevé |
| 🔴 **Haute** | Enrichissement secteur | Élevé | Très élevé |
| 🟡 **Moyenne** | Comparateur entreprises | Moyen | Élevé |
| 🟡 **Moyenne** | Export données | Faible | Moyen |
| 🟢 **Basse** | Machine Learning | Très élevé | Moyen |
| 🟢 **Basse** | API REST | Élevé | Moyen |

**Recommandation** : Commencer par les filtres dynamiques et l'enrichissement des données par secteur pour maximiser l'impact utilisateur.

---

## 📜 Copyright

### Déclaration d'originalité

**Je/Nous déclarons sur l'honneur que le code fourni a été produit par moi/nous-même(s), à l'exception des éléments listés ci-dessous.**

### Code emprunté et sources

Toutes les lignes ou groupes de lignes empruntés à des sources externes sont déclarés ici avec leurs références :

#### 1. Framework Dash - Structure de base

**Fichier** : `main.py`, lignes 1-30  
**Source** : [Documentation officielle Dash](https://dash.plotly.com/layout)  
**Explication** : Structure de base d'une application Dash avec `app = Dash(__name__)` et `app.layout`. Syntaxe standard du framework.

#### 2. Plotly - Configuration des graphiques

**Fichier** : `src/components/component1.py`, lignes 15-25  
**Source** : [Documentation Plotly Subplots](https://plotly.com/python/subplots/)  
**Explication** : Utilisation de `make_subplots()` pour créer plusieurs graphiques empilés. Syntaxe officielle de Plotly pour les sous-graphiques.

```python
fig = make_subplots(rows=n, cols=1, subplot_titles=[...])
```

#### 3. Pandas - Groupby et agrégations

**Fichier** : `src/components/component2.py`, ligne 12  
**Source** : [Documentation Pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)  
**Explication** : Agrégation par groupe avec `.groupby().mean().reset_index()`. Syntaxe standard Pandas.

```python
means = df.groupby(SIZE_COLUMN)[NOTE_COLUMNS].mean().reset_index()
```

#### 4. Plotly Express - Animations

**Fichier** : `src/components/component3.py`, lignes 10-20  
**Source** : [Plotly Animation Documentation](https://plotly.com/python/animations/)  
**Explication** : Paramètre `animation_frame` pour créer des animations temporelles dans Plotly Express.

```python
fig = px.scatter(df, animation_frame=YEAR_COLUMN, ...)
```

#### 5. CSS - Flexbox pour le footer

**Fichier** : `src/components/footer.py`, lignes 50-55  
**Source** : [MDN Web Docs - Flexbox](https://developer.mozilla.org/fr/docs/Web/CSS/CSS_Flexible_Box_Layout)  
**Explication** : Utilisation de `display: flex` et `justifyContent: 'space-around'` pour aligner les éléments du footer.

```python
style={'display': 'flex', 'justifyContent': 'space-around'}
```

#### 7. SQLAlchemy - ORM et connexion SQLite

**Fichier** : `db.py`, lignes 8-10  
**Source** : [Documentation SQLAlchemy](https://docs.sqlalchemy.org/en/20/core/engines.html)  
**Explication** : Création d'un moteur SQLAlchemy pour se connecter à SQLite. `create_engine()` avec le paramètre `future=True` active le mode SQLAlchemy 2.0.

```python
from sqlalchemy import create_engine
engine = create_engine(DB_URL, future=True)
```

#### 8. Pandas - Lecture/Écriture SQL

**Fichier** : `db.py`, lignes 18-20 et 26-28  
**Source** : [Pandas SQL Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)  
**Explication** : Utilisation de `to_sql()` pour écrire un DataFrame dans SQLite et `read_sql()` pour lire depuis une table SQL.

```python
df.to_sql(table, engine, if_exists="replace", index=False)
df = pd.read_sql(f"SELECT * FROM {table}", con=engine)
```

#### 9. Requests - Téléchargement HTTP

**Fichier** : `src/utils/get_data.py`, lignes 20-25  
**Source** : [Documentation Requests](https://requests.readthedocs.io/)  
**Explication** : Utilisation de `requests.get()` pour télécharger un fichier depuis une URL et `response.content` pour récupérer les données binaires.

```python
response = requests.get(DATA_URL)
with open(EXCEL_PATH, "wb") as f:
    f.write(response.content)
```

#### 10. Regex - Extraction de nombres

**Fichier** : `src/utils/clean_data.py`, lignes 20-25  
**Source** : [Python re module](https://docs.python.org/3/library/re.html)  
**Explication** : Expression régulière `r"\d+(\.\d+)?"` pour extraire le premier nombre décimal d'une chaîne. Utilisé pour nettoyer les colonnes de notes.

```python
match = re.search(r"\d+(\.\d+)?", str(val))
if match:
    return float(match.group())
```

### Déclaration finale

**Toute ligne non déclarée ci-dessus est réputée être produite par l'auteur (ou les auteurs) du projet.**

L'absence ou l'omission de déclaration sera considérée comme du plagiat.

**Auteurs** :
- OUCHAOU Lina
- POGEANT Justine

**Date** : Novembre 2025  
**Projet** : Dashboard Égalité Professionnelle - Python 2025

---

<div align="center">

**Fait avec ❤️ par OUCHAOU Lina & POGEANT Justine**

*Dashboard Égalité Professionnelle 2025*

---

📧 Contact : [lina.ouchaou@edu.esiee.fr](lina.ouchaou@edu.esiee.fr) et [justine.pogeant@edu.esiee.fr](justine.pogeant@edu.esiee.fr)

💻 GitHub : [https://github.com/LinaOuchaouAmroussi/projet_data.git](https://github.com/LinaOuchaouAmroussi/projet_data.git)

</div>