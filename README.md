# 🏠 Dashboard Égalité Professionnelle

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-2.14+-purple?logo=plotly&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.17+-blue?logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

**Analyse et visualisation des données d'égalité professionnelle dans les entreprises françaises**

[Démo](#-fonctionnalités) • [Installation](#-installation) • [Utilisation](#-utilisation) • [Documentation](#-structure-du-projet)

</div>

---

## 📋 Table des matières

- [À propos](#-à-propos)
- [Fonctionnalités](#-fonctionnalités)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Structure du projet](#-structure-du-projet)
- [Technologies](#-technologies)
- [Auteurs](#-auteurs)
- [Licence](#-licence)

---

## 📖 À propos

Ce dashboard interactif permet d'explorer et d'analyser les données de l'**Index Égalité Professionnelle** des entreprises françaises de plus de 50 salariés. 

Le jeu de données rassemble les scores attribués chaque année aux entreprises françaises sur leur niveau d'égalité entre les femmes et les hommes. Cet index, noté sur 100 points, mesure notamment :
- Les écarts de rémunération 💰
- Les écarts d'augmentation et de promotion 📈
- Les retours de congé maternité 👶
- La présence équilibrée de femmes et d'hommes parmi les plus hautes rémunérations 👔

Ce dashboard permet d'identifier les entreprises qui doivent mettre en place des actions correctives pour améliorer l'égalité professionnelle.

---

## ✨ Fonctionnalités

### 🏠 Page d'accueil
Tableau de bord principal avec présentation du projet et accès rapide aux différentes analyses via des cartes interactives.

### 📊 Distribution des Notes
- Histogrammes de distribution pour chaque catégorie de notes
- Visualisation de la répartition des entreprises par score
- Analyse détaillée par indicateur d'égalité

### 📈 Notes moyennes par taille d'entreprise
- Comparaison des performances selon la taille (50-250, 251-999, 1000+)
- Identification des tendances par catégorie d'effectifs
- Graphiques en barres interactifs

### 🗺️ Évolution temporelle animée par région
- Animation de l'évolution des notes année par année
- Coloration par région pour identifier les disparités géographiques
- Graphique scatter interactif avec contrôles d'animation

### 📉 Évolution par taille d'entreprise
- Courbes d'évolution temporelle animées
- Comparaison des trajectoires selon la taille
- Animation fluide avec contrôles de lecture

### 📑 Statistiques clés
- Métriques globales et indicateurs de performance
- Tableaux de synthèse
- Analyses statistiques détaillées

### 🗺️ Carte interactive de l'égalité professionnelle
- Visualisation géographique des données
- Exploration par région
- Filtres et interactions dynamiques

---

## 🚀 Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- Git (optionnel)

### Étape 1 : Cloner le projet

```bash
git clone https://github.com/votre-username/data_project.git
cd data_project
```

Ou téléchargez le projet et décompressez-le.

### Étape 2 : Créer un environnement virtuel

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

### Étape 3 : Installer les dépendances

```bash
pip install -r requirements.txt
```

### Étape 4 : Vérifier les données ??? JSP SI BESOIN DU COUP

Assurez-vous que le fichier `data/cleaned/cleaneddata.csv` est présent. Si ce n'est pas le cas, placez vos données dans ce dossier.

---

## 🎯 Utilisation

### Lancer le dashboard complet

```bash
python main.py
```

Le dashboard sera accessible sur : **http://127.0.0.1:8050/**


### Navigation

Une fois le dashboard lancé :

1. 🏠 **Page d'accueil** : Vue d'ensemble et accès aux analyses
2. 📊 Cliquez sur les cartes pour accéder aux visualisations
3. 🔍 Survolez les graphiques pour voir les détails
4. ▶️ Utilisez les contrôles d'animation sur les graphiques temporels
5. 🔙 Utilisez "Retour à l'accueil" pour naviguer

---

## 📁 Structure du projet

```
data_project
|-- .gitignore
|-- .venv
|   |-- *
|-- config.py                                   # fichier de configuration
|-- main.py                                     # fichier principal permettant de lancer le dashboard
|-- requirements.txt                            # liste des packages additionnels requis
|-- README.md
|-- data                                        # les données
│   |-- cleaned
│   │   |-- cleaneddata.csv
│   |-- raw
│       |-- rawdata.csv
|-- images                                      # images utilisées dans le README
|-- src                                         # le code source du dashboard
|   |-- components                              # les composants du dashboard
|   |   |-- __init__.py
|   |   |-- component1.py
|   |   |-- component2.py
|   |   |-- footer.py
|   |   |-- header.py
|   |   |-- navbar.py
|   |-- pages                                   # les pages du dashboard
|   |   |-- __init__.py
|   |   |-- simple_page.py
|   |   |-- more_complex_page
|   |   |   |-- __init__.py
|   |   |   |-- layout.py
|   |   |   |-- page_specific_component.py
|   |   |-- home.py
|   |   |-- about.py
|   |-- utils                                   # les fonctions utilitaires
|   |   |-- __init__.py
|   |   |-- common_functions.py
|   |   |-- get_data.py                         # script de récupération des données
|   |   |-- clean_data.py                       # script de nettoyage des données
|-- video.mp4

## 🛠️ Technologies

### Langages et Frameworks

- **Python 3.12** - Langage de programmation
- **Dash 2.14+** - Framework web pour applications analytiques
- **Plotly 5.17+** - Bibliothèque de visualisation interactive

### Bibliothèques principales

```python
dash>=2.14.0              # Framework dashboard
plotly>=5.17.0            # Visualisations interactives
pandas>=2.0.0             # Manipulation de données
numpy>=1.24.0             # Calculs numériques
```

### Outils de développement

- **Git** - Contrôle de version
- **VS Code** - Éditeur de code
- **pip** - Gestionnaire de paquets

---

## 📊 Format des données

Le fichier `cleaneddata.csv` doit contenir les colonnes suivantes :

| Colonne | Description | Type |
|---------|-------------|------|
| `note_index` | Note globale d'égalité professionnelle | float |
| `note_ecart_rémunération` | Note sur les écarts de rémunération | float |
| `note_ecart_taux_d'augmentation_(hors_promotion)` | Note sur les augmentations | float |
| `note_ecart_taux_de_promotion` | Note sur les promotions | float |
| `note_retour_congé_maternité` | Note sur le retour de congé maternité | float |
| `note_hautes_rémunérations` | Note sur les hautes rémunérations | float |
| `tranche_d'effectifs` | Taille de l'entreprise | string |
| `année` | Année de déclaration | int |
| `région` | Région de l'entreprise | string |

---

## 🎨 Personnalisation

### Modifier les couleurs

Dans `src/components/config.py` ou dans chaque composant :

```python
# Couleur principale (bleu foncé)
PRIMARY_COLOR = '#1f4788'

# Couleurs des graphiques
CHART_COLORS = ['#5470C6', '#91CC75', '#FAC858']
```

### Ajouter une nouvelle page

1. Créez `src/pages/ma_nouvelle_page.py`
2. Importez dans `main.py`
3. Ajoutez le lien dans la navigation

### Modifier le footer

Éditez `src/components/footer.py` pour changer les informations de contact, liens, etc.

---

## 🐛 Résolution de problèmes

### Le dashboard ne se lance pas

```bash
# Vérifier que l'environnement virtuel est activé
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate

# Réinstaller les dépendances
pip install -r requirements.txt
```

### Erreur "Module not found"

```bash
# Vérifier que les fichiers __init__.py existent
ls src/__init__.py
ls src/components/__init__.py
ls src/pages/__init__.py

# Si manquants, les créer
touch src/__init__.py src/components/__init__.py src/pages/__init__.py
```

### Données non trouvées

```bash
# Vérifier le chemin du fichier
ls data/cleaned/cleaneddata.csv

# Si absent, placez vos données au bon endroit
```

### Port déjà utilisé

Si le port 8050 est occupé, modifiez dans `main.py` :

```python
app.run(debug=True, port=8051)  # Changez le port
```

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche (`git checkout -b feature/amelioration`)
3. Committez vos changements (`git commit -m 'Ajout amélioration'`)
4. Pushez vers la branche (`git push origin feature/amelioration`)
5. Ouvrez une Pull Request

---

## 👥 Auteurs

- **OUCHAOU Lina** - Développement et analyse
- **POGEANT Justine** - Développement et analyse

**Projet Python 2025** - Formation Data Science

---

## 📜 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

## 📚 Ressources

- [Documentation Dash](https://dash.plotly.com/)
- [Documentation Plotly](https://plotly.com/python/)
- [Documentation Pandas](https://pandas.pydata.org/)
- [Index Égalité Professionnelle - data.gouv.fr](https://www.data.gouv.fr/)

---

## 📞 Contact

Pour toute question ou suggestion :

- 📧 Email : lina.ouchaou@edu.esiee.fr et justine.pogeant@edu.esiee.fr


---

<div align="center">

**Fait avec ❤️ par OUCHAOU Lina & POGEANT Justine**

*Dashboard Égalité Professionnelle - 2024-2025*

</div>