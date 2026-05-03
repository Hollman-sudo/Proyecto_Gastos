# comparar_presupuesto.py
# Compara presupuesto vs gasto real y devuelve la diferencia y un mensaje

def comparar_presupuesto(presupuesto, gasto_real):
    """
    Recibe presupuesto (número) y gasto_real (número).
    Devuelve (diferencia, texto_estado)
    diferencia = presupuesto - gasto_real
    """
    diferencia = presupuesto - gasto_real
    
    if diferencia > 0:
        estado = f"ahorraste ${diferencia:.0f}"
    elif diferencia < 0:
        estado = f"te excediste por ${-diferencia:.0f}"
    else:
        estado = "gastaste exactamente lo presupuestado"
    
    return diferencia, estado