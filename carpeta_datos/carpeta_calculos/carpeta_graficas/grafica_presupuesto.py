# grafica_presupuesto.py
# Compara presupuesto y gasto real con un gráfico de barras

import matplotlib.pyplot as plt

def graficar_comparativa_presupuesto(presupuesto, gasto_real):
    """
    Recibe dos números: presupuesto y gasto real.
    Muestra un gráfico de dos barras.
    """
    # Nombres de las barras y sus valores
    categorias = ['Presupuesto', 'Gasto Real']
    valores = [presupuesto, gasto_real]
    colores = ['green', 'orange']
    
    plt.figure(figsize=(6, 5))
    plt.bar(categorias, valores, color=colores)
    
    plt.title('Comparativa: Presupuesto planeado vs Gasto real')
    plt.ylabel('Monto ($)')
    
    plt.show()