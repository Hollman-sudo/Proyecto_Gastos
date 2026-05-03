# entrada_tabla_de_datos.py
# Este módulo se encarga de leer el archivo CSV con las transacciones

import pandas as pd

def cargar_datos(ruta_archivo):
    """
    Lee un archivo CSV con columnas: dia, categoria, monto.
    Retorna un DataFrame de pandas o None si hay error.
    """
    try:
        # Intentar leer el archivo
        df = pd.read_csv(ruta_archivo)
        
        # Verificar que tenga las columnas necesarias
        columnas_requeridas = {'dia', 'categoria', 'monto'}
        if not columnas_requeridas.issubset(df.columns):
            print(f"❌ Error: El archivo debe tener las columnas {columnas_requeridas}")
            return None
        
        # Asegurar que la columna monto sea número
        df['monto'] = pd.to_numeric(df['monto'], errors='coerce')
        
        # Eliminar filas donde el monto no sea válido (por si acaso)
        df = df.dropna(subset=['monto'])
        
        print(f"✅ Datos cargados correctamente. {len(df)} transacciones encontradas.")
        return df
        
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo: {ruta_archivo}")
        return None
    except Exception as e:
        print(f"❌ Error inesperado al leer el archivo: {e}")
        return None