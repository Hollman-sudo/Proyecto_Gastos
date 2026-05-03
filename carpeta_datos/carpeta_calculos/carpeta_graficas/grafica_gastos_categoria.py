# grafica_gastos_categoria.py
# Crea un gráfico de barras con los montos por categoría

import matplotlib.pyplot as plt

def graficar_gastos_categoria(diccionario_gastos):
    """
    Recibe un diccionario {categoria: monto}
    Muestra una ventana con el gráfico.
    """
    # Extraer las listas de categorías y montos
    categorias = list(diccionario_gastos.keys())
    montos = list(diccionario_gastos.values())
    
    # Crear la figura (tamaño ancho=8, alto=5 pulgadas)
    plt.figure(figsize=(8, 5))
    
    # Dibujar barras verticales, color celeste
    plt.bar(categorias, montos, color='skyblue')
    
    # Títulos y etiquetas
    plt.title('Gastos por categoría - Mes actual')
    plt.xlabel('Categoría')
    plt.ylabel('Monto gastado ($)')
    
    # Mostrar el gráfico
    plt.show()