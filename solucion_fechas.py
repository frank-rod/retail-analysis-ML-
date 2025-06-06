import pandas as pd
import numpy as np

# Función para convertir fechas de forma robusta
def convertir_fechas_robusta(df):
    """
    Convierte fechas manejando diferentes formatos posibles
    """
    print("📅 Convirtiendo fechas de forma robusta...")
    
    # Intentar diferentes métodos de conversión
    try:
        # Método 1: Formato europeo (DD/MM/YYYY)
        df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], dayfirst=True, errors='coerce')
        print("✅ Fechas convertidas con formato europeo (DD/MM/YYYY)")
        
    except Exception as e:
        try:
            # Método 2: Formato mixto
            df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='mixed', errors='coerce')
            print("✅ Fechas convertidas con formato mixto")
            
        except Exception as e2:
            try:
                # Método 3: Inferir formato automáticamente
                df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], infer_datetime_format=True, errors='coerce')
                print("✅ Fechas convertidas con inferencia automática")
                
            except Exception as e3:
                print(f"❌ Error en conversión de fechas: {e3}")
                return None
    
    # Verificar resultados
    fechas_nulas = df['InvoiceDate'].isnull().sum()
    if fechas_nulas > 0:
        print(f"⚠️ {fechas_nulas} fechas no se pudieron convertir")
        # Eliminar filas con fechas nulas
        df = df.dropna(subset=['InvoiceDate'])
        print(f"🧹 Eliminadas {fechas_nulas} filas con fechas inválidas")
    
    print(f"📊 Rango final: {df['InvoiceDate'].min()} a {df['InvoiceDate'].max()}")
    return df

# Cargar y procesar datos
print("📁 Cargando archivo...")
df = pd.read_csv('Online Retail.csv', encoding='latin-1')

# Limpiar nombres de columnas
df.columns = ['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country']

print(f"📊 Datos originales: {df.shape}")
print(f"🗓️ Muestra de fechas antes de conversión:")
print(df['InvoiceDate'].head(10))

# Convertir fechas
df = convertir_fechas_robusta(df)

if df is not None:
    print(f"✅ Conversión exitosa. Datos finales: {df.shape}")
    print("🎯 Usa este código en tu notebook:")
    print("="*50)
    print("# Convertir fechas - MÉTODO ROBUSTO")
    print("df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], dayfirst=True, errors='coerce')")
    print("df = df.dropna(subset=['InvoiceDate'])  # Eliminar fechas inválidas")
    print("="*50)
else:
    print("❌ No se pudo convertir las fechas") 