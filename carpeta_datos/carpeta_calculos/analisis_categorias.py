# analisis_categorias.py
# Módulo para analizar gastos por categoría

def gastos_por_categoria(df):
    """
    Recibe un DataFrame con columna 'categoria' y 'monto'.
    Retorna un diccionario {categoria: total_gastado}
    """
    gastos = df.groupby('categoria')['monto'].sum().to_dict()
    return gastos

def categoria_mayor_gasto(diccionario_gastos):
    """
    Recibe un diccionario {categoria: monto}
    Retorna la categoría con mayor monto y su valor.
    """
    if not diccionario_gastos:
        return None, 0
    mayor_categoria = max(diccionario_gastos, key=diccionario_gastos.get)
    mayor_monto = diccionario_gastos[mayor_categoria]
    return mayor_categoria, mayor_monto