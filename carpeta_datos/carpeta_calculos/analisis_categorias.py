# analisis_categorias.py
# Funciones para agrupar gastos por categoría

def gastos_por_categoria(dataframe):
    """
    Recibe un DataFrame con columnas 'categoria' y 'monto'.
    Devuelve un diccionario {nombre_categoria: total_gastado}
    """
    # groupby agrupa por categoria, sum suma los montos, to_dict convierte a diccionario
    resultado = dataframe.groupby('categoria')['monto'].sum().to_dict()
    return resultado

def categoria_mayor_gasto(diccionario_gastos):
    """
    Recibe un diccionario {categoria: monto}
    Devuelve (categoria_con_mayor_monto, monto_maximo)
    """
    if not diccionario_gastos:   # si el diccionario está vacío
        return None, 0
    
    # max con key= obtiene la clave cuyo valor es mayor
    mayor = max(diccionario_gastos, key=diccionario_gastos.get)
    monto = diccionario_gastos[mayor]
    return mayor, monto