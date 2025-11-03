import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Chemin absolu vers le dossier projet_data
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Chemins d'accès vers le même dossier que carte_egalite.html
CLEANED_DIR = os.path.join(PROJECT_DIR, "data", "cleaned")
OUTPUTS_DIR = os.path.join(PROJECT_DIR, "data", "outputs")  # Changé pour pointer vers le dossier outputs du projet
CLEANED_DATA = os.path.join(CLEANED_DIR, "cleaneddata.csv")  # Ajout du chemin vers le fichier CSV

# Créer le dossier output s'il n'existe pas
os.makedirs(OUTPUTS_DIR, exist_ok=True)

class DataVisualizations:
    def __init__(self, data: pd.DataFrame):
        """
        Initialise la classe avec les données.
        
        Args:
            data (pd.DataFrame): DataFrame contenant les données nettoyées
        """
        self.data = data  # Stocke les données comme attribut de classe
        
        # Définition des colonnes pour les visualisations
        self.note_columns = [
            'note_ecart_rémunération',
            'note_ecart_taux_d\'augmentation_(hors_promotion)',
            'note_ecart_taux_de_promotion',
            'note_ecart_taux_d\'augmentation',
            'note_retour_congé_maternité',
            'note_hautes_rémunérations',
            'note_index'
        ]
        self.size_column = 'tranche_d\'effectifs'
        self.year_column = 'année'
        self.region_column = 'région'

    def plot_note_distribution(self):
        """Distribution des notes par catégorie"""
        valid_columns = [col for col in self.note_columns if col in self.data.columns]
        
        fig = make_subplots(
            rows=len(valid_columns), 
            cols=1,
            subplot_titles=[col.replace('_', ' ').title() for col in valid_columns]
        )
        
        for i, col in enumerate(valid_columns, 1):
            valid_data = self.data[col].dropna()
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

    def plot_note_by_size_dynamic(self):
        """Notes moyennes par taille d'entreprise"""
        # Calculer les moyennes par taille d'entreprise
        means = self.data.groupby(self.size_column)[self.note_columns].mean().reset_index()
        
        fig = px.bar(
            means, 
            x=self.size_column,
            y='note_index',
            title="Note Moyenne d'Égalité Professionnelle selon la Taille de l'Entreprise",
            labels={
                self.size_column: "Taille de l'entreprise",
                'note_index': "Note moyenne globale"
            }
        )
        
        fig.update_layout(
            xaxis_title="Tranche d'effectifs",
            yaxis_title="Note moyenne",
            title_x=0.5
        )
        
        return fig

    def plot_evolution_temporelle_animated(self):
        """Évolution temporelle des notes avec animation"""
        fig = px.scatter(
            self.data, 
            x='note_index',
            y='note_ecart_rémunération',
            animation_frame=self.year_column,
            color=self.region_column,
            title="Évolution des Notes d'Égalité Professionnelle par Année et Région",
            labels={
                'note_index': "Note globale",
                'note_ecart_rémunération': "Note écart de rémunération",
                self.region_column: "Région",
                self.year_column: "Année"
            }
        )
        
        fig.update_layout(
            title_x=0.5,
            showlegend=True
        )
        
        return fig

    def plot_evolution_by_size_animated(self):
        """Évolution des notes par taille d'entreprise avec animation"""
        # Calculer les moyennes par année et taille
        means = (self.data.groupby([self.year_column, self.size_column])
                ['note_index'].mean().reset_index())
        
        fig = px.line(
            means, 
            x=self.size_column,
            y='note_index',
            animation_frame=self.year_column,
            title="Évolution de la Note Moyenne par Taille d'Entreprise",
            labels={
                self.size_column: "Taille de l'entreprise",
                'note_index': "Note moyenne",
                self.year_column: "Année"
            }
        )
        
        fig.update_layout(
            title_x=0.5,
            xaxis_title="Tranche d'effectifs",
            yaxis_title="Note moyenne",
            showlegend=True
        )
        
        # Ajouter des marqueurs pour mieux voir les points
        fig.update_traces(mode='lines+markers')
        
        return fig

    def create_dashboard_summary(self):
        """Crée un résumé statistique des données"""
        return {
            "Note Moyenne Globale": self.data["note_index"].mean(),
            "Nombre d'Entreprises": len(self.data),
            "Années Couvertes": f"{self.data['année'].min()} - {self.data['année'].max()}",
            "Note Maximale": self.data["note_index"].max(),
            "Note Minimale": self.data["note_index"].min()
        }

    def create_stats_visualization(self):
        """Crée une visualisation HTML des statistiques"""
        stats = self.create_dashboard_summary()
        
        # Créer une figure avec une table stylisée
        fig = go.Figure(data=[go.Table(
            header=dict(
                values=['Indicateur', 'Valeur'],
                fill_color='#2874A6',
                align='left',
                font=dict(color='white', size=16)
            ),
            cells=dict(
                values=[
                    list(stats.keys()),
                    [f"{v:.2f}" if isinstance(v, (int, float)) else str(v) for v in stats.values()]
                ],
                fill_color='#EBF5FB',
                align='left',
                font=dict(color='black', size=14)
            )
        )])
        
        # Mise en page
        fig.update_layout(
            title=dict(
                text="Tableau de Bord - Statistiques Clés",
                x=0.5,
                y=0.95,
                font=dict(size=24)
            ),
            width=800,
            height=400,
            showlegend=False
        )
        
        return fig


# Fonction pour intégrer dans main.py ou un component
def generate_visualizations(df):
    """
    Fonction helper pour générer toutes les visualisations
    Args:
        df: DataFrame nettoyé
    Returns:
        dict: Dictionnaire contenant toutes les figures
    """
    viz = DataVisualizations(df)
    
    return {
        "distribution": viz.plot_note_distribution(),
        "note_by_size": viz.plot_note_by_size_dynamic(),
        "evolution_temporelle": viz.plot_evolution_temporelle_animated(),
        "evolution_by_size": viz.plot_evolution_by_size_animated(),
        "summary_stats": viz.create_dashboard_summary()
    }


# Exemple d'utilisation dans un script de test
if __name__ == "__main__":
    # Charger les données
    df = pd.read_csv(CLEANED_DATA)
    viz = DataVisualizations(df)
    
    # Sauvegarder dans le même dossier que carte_egalite.html
    viz.plot_note_distribution().write_html(os.path.join(OUTPUTS_DIR, "distribution.html"))
    viz.plot_note_by_size_dynamic().write_html(os.path.join(OUTPUTS_DIR, "note_by_size.html"))
    viz.plot_evolution_temporelle_animated().write_html(os.path.join(OUTPUTS_DIR, "evolution_temporelle.html"))
    viz.plot_evolution_by_size_animated().write_html(os.path.join(OUTPUTS_DIR, "evolution_by_size.html"))
    
    # Remplacer la sauvegarde du fichier texte par la visualisation HTML
    viz.create_stats_visualization().write_html(
        os.path.join(OUTPUTS_DIR, "statistics.html"),
        full_html=True,
        include_plotlyjs=True
    )
    
    print(f"Visualisations sauvegardées dans {OUTPUTS_DIR}")