import pandas as pd

# Lire le fichier Excel
excel_file = "index.xlsx"
df = pd.read_excel(excel_file)

# Afficher un aperçu des données
print(df.head())

# Sauvegarder en CSV
csv_file = "index.csv"
df.to_csv(csv_file, index=False)  # index=False pour ne pas ajouter la colonne d'index
