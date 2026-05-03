# gastos_mayor_total.py
# Módulo para encontrar el día de mayor gasto y el total del mes

def dia_mayor_gasto(df):
    """
    Recibe un DataFrame con columna 'dia' y 'monto'.
    Retorna el número del día con mayor gasto acumulado y el monto.
    """
    # Agrupar por día y sumar montos
    gastos_por_dia = df.groupby('dia')['monto'].sum()
    
    # Encontrar el día con mayor gasto
    dia_max = gastos_por_dia.idxmax()  # índice (día)
    monto_max = gastos_por_dia.max()   # valor máximo
    return dia_max, monto_max

def gasto_total_mes(df):
    """
    Recibe un DataFrame con columna 'monto'.
    Retorna la suma total de todos los gastos.
    """
    total = df['monto'].sum()
    return total