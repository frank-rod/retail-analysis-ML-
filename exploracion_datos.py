import pandas as pd
import numpy as np

# Leer el archivo CSV
print("Cargando archivo CSV...")
df = pd.read_csv('Online Retail.csv', encoding='latin-1')

# Información básica sobre el dataset
print(f"Forma del dataset: {df.shape}")
print(f"Columnas: {list(df.columns)}")
print("\nPrimeras 5 filas:")
print(df.head())

print("\nInformación del dataset:")
print(df.info())

print("\nValores nulos por columna:")
print(df.isnull().sum())

print("\nEstadísticas descriptivas:")
print(df.describe())

print("\nPrimeros valores únicos de algunas columnas clave:")
if 'Country' in df.columns:
    print(f"\nPaíses únicos: {df['Country'].nunique()}")
    print(f"Países más frecuentes:\n{df['Country'].value_counts().head()}")

if 'Description' in df.columns:
    print(f"\nProductos únicos: {df['Description'].nunique()}")
    print(f"Productos más frecuentes:\n{df['Description'].value_counts().head()}") 