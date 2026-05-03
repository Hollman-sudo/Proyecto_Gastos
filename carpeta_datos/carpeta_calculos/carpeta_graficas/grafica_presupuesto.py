# grafica_presupuesto.py
# Gráfico comparativo entre presupuesto y gasto real

import matplotlib.pyplot as plt

def graficar_comparativa_presupuesto(presupuesto, gasto_real):
    """
    Muestra un gráfico de barras comparando presupuesto vs gasto real.
    """
    categorias = ['Presupuesto', 'Gasto Real']
    valores = [presupuesto, gasto_real]
    colores = ['green', 'orange']
    
    plt.figure(figsize=(6, 5))
    barras = plt.bar(categorias, valores, color=colores)
    
    plt.title('Comparativa: Presupuesto planeado vs Gasto real', fontsize=12)
    plt.ylabel('Monto ($)')
    
    # Etiquetas con los valores
    for barra in barras:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2., altura + 100,
                 f'${altura:,.0f}', ha='center', va='bottom')
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()