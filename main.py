# main.py
# Programa principal para el análisis de gastos de Felipe.
# Este programa lee un archivo CSV con sus transacciones, debe estar en la raiz de lña carpeta para poder leerlo.
# calcula estadísticas, compara con su presupuesto y genera gráficos.

# ---------------------------------------------------------------------
# 1. Importar módulos necesarios
# ---------------------------------------------------------------------

import sys  # Para poder agregar las carpetas al camino de búsqueda de Python

# Agregamos las carpetas donde tenemos nuestros módulos personales.
# sys.path.append le dice a Python: "busca también dentro de estas carpetas".
sys.path.append('carpeta_datos')
sys.path.append('carpeta_datos/carpeta_calculos')
sys.path.append('carpeta_datos/carpeta_calculos/carpeta_graficas')

# Ahora importamos las funciones que creamos en cada archivo.
from entrada_tabla_de_datos import cargar_datos
from entrada_presupuesto import pedir_presupuesto
from analisis_categorias import gastos_por_categoria, categoria_mayor_gasto
from gastos_mayor_total import dia_mayor_gasto, gasto_total_mes
from comparar_presupuesto import comparar_presupuesto
from grafica_gastos_categoria import graficar_gastos_categoria
from grafica_presupuesto import graficar_comparativa_presupuesto

# ---------------------------------------------------------------------
# 2. Función principal (orquesta todo el programa)
# ---------------------------------------------------------------------

def main():
    """
    Flujo completo del análisis:
    - Pide el archivo CSV al usuario
    - Carga los datos
    - Calcula gastos por categoría, día mayor gasto, total del mes
    - Pide presupuesto y compara
    - Muestra gráficos
    """

    print("\n=== Análisis de Gastos ===\n")

    # ----- Paso 1: Solicitar el archivo de transacciones -----
    # Felipe debe escribir el nombre de su archivo (ej: "mis_gastos.csv")
    # El archivo debe estar en la misma carpeta que este programa.
    archivo = input("Ingresa el nombre del archivo CSV con tus transacciones: ")

    # ----- Paso 2: Cargar los datos -----
    # La función cargar_datos intenta leer el CSV y devuelve un DataFrame.
    # Si hay error (archivo no existe, columnas incorrectas), devuelve None.
    df = cargar_datos(archivo)

    # Si hubo error, terminamos el programa sin hacer más nada.
    if df is None:
        return

    # Mostramos cuántas transacciones se cargaron (filas del CSV)
    print(f"Se cargaron {len(df)} transacciones.\n")

    # ----- Paso 3: Calcular gastos por categoría -----
    # gastos_por_categoria devuelve un diccionario como:
    # {"comida": 123000, "transporte": 48000, ...}
    gastos_cat = gastos_por_categoria(df)

    print("Gastos por categoría:")
    for categoria, monto in gastos_cat.items():
        # El formato :,.0f muestra el número con separadores de miles y sin decimales
        print(f"  {categoria}: ${monto:,.0f}")

    # ----- Paso 4: Identificar la categoría con mayor gasto -----
    mayor_cat, mayor_monto = categoria_mayor_gasto(gastos_cat)
    print(f"\nCategoría con mayor gasto: {mayor_cat} (${mayor_monto:,.0f})")

    # ----- Paso 5: Día de mayor gasto y total del mes -----
    dia_max, monto_dia = dia_mayor_gasto(df)
    print(f"Día de mayor gasto: día {dia_max} con ${monto_dia:,.0f}")

    total_mes = gasto_total_mes(df)
    print(f"Total gastado en el mes: ${total_mes:,.0f}")

    # ----- Paso 6: Pedir presupuesto al usuario -----
    # La función pedir_presupuesto valida que sea un número positivo.
    presupuesto = pedir_presupuesto()

    # ----- Paso 7: Comparar presupuesto con gasto real -----
    diferencia, estado = comparar_presupuesto(presupuesto, total_mes)
    print(f"\nPresupuesto: ${presupuesto:,.0f}  |  Gasto real: ${total_mes:,.0f}")
    print(f"Diferencia: ${abs(diferencia):,.0f} ({estado})")

    # ----- Paso 8: Generar gráficos -----
    # Grafico de barras: gastos por categoría
    graficar_gastos_categoria(gastos_cat)

    # Grafico comparativo: presupuesto vs gasto real
    graficar_comparativa_presupuesto(presupuesto, total_mes)

    print("\nAnálisis completado. Cierra las ventanas de los gráficos para terminar.")

# ---------------------------------------------------------------------
# 3. Ejecutar la función principal solo si este archivo es el punto de entrada
# ---------------------------------------------------------------------
# Esta condición es estándar en Python: si ejecutamos directamente este archivo,
# entonces se llama a main(). Si alguien importa este archivo como módulo,
# no se ejecuta automáticamente.
if __name__ == "__main__":
    main()