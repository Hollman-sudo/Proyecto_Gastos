# gastos_mayor_total.py
# Funciones para calcular el día con más gastos y la suma total

def dia_mayor_gasto(dataframe):
    """
    Recibe un DataFrame con columnas 'dia' y 'monto'.
    Retorna (numero_dia, monto_total_de_ese_dia)
    """
    # Agrupar por día y sumar los montos
    gastos_por_dia = dataframe.groupby('dia')['monto'].sum()
    
    # idxmax() devuelve el índice (el día) con mayor suma
    dia_max = gastos_por_dia.idxmax()
    # max() devuelve el valor máximo
    monto_max = gastos_por_dia.max()
    return dia_max, monto_max

def gasto_total_mes(dataframe):
    """
    Recibe un DataFrame con columna 'monto'.
    Retorna la suma de todos los montos.
    """
    total = dataframe['monto'].sum()
    return total