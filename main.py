# main.py - Punto de entrada del programa de análisis de gastos

import sys

# Agregar las carpetas al path (con los nombres reales en minúsculas)
sys.path.append('carpeta_datos')
sys.path.append('carpeta_datos/carpeta_calculos')
sys.path.append('carpeta_datos/carpeta_calculos/carpeta_graficas')

# Importar funciones - nombres exactos sin tildes
from entrada_tabla_de_datos import cargar_datos
from entrada_presupuesto import pedir_presupuesto
from analisis_categorias import gastos_por_categoria, categoria_mayor_gasto
from gastos_mayor_total import dia_mayor_gasto, gasto_total_mes
from comparar_presupuesto import comparar_presupuesto
from grafica_gastos_categoria import graficar_gastos_categoria
from grafica_presupuesto import graficar_comparativa_presupuesto

def main():
    print("=== Análisis de Gastos para Felipe ===\n")
    
    # 1. Cargar datos
    archivo = "transacciones_ejemplo.csv"
    df = cargar_datos(archivo)
    if df is None:
        return
    
    # 2. Mostrar información básica
    print(f"\nSe cargaron {len(df)} transacciones.")
    
    # 3. Calcular gastos por categoría
    gastos_cat = gastos_por_categoria(df)
    print("\nGastos por categoría:")
    for cat, monto in gastos_cat.items():
        print(f"  {cat}: ${monto:,.0f}")
    
    mayor_cat, mayor_monto = categoria_mayor_gasto(gastos_cat)
    print(f"\n📊 Categoría con mayor gasto: {mayor_cat} (${mayor_monto:,.0f})")
    
    # 4. Día de mayor gasto y total del mes
    dia_max, monto_max = dia_mayor_gasto(df)
    print(f"📅 Día de mayor gasto: día {dia_max} con ${monto_max:,.0f}")
    
    total_mes = gasto_total_mes(df)
    print(f"💰 Gasto total del mes: ${total_mes:,.0f}")
    
    # 5. Pedir presupuesto
    presupuesto = pedir_presupuesto()
    
    # 6. Comparar
    diferencia, estado = comparar_presupuesto(presupuesto, total_mes)
    print(f"\nPresupuesto: ${presupuesto:,.0f} | Gasto real: ${total_mes:,.0f}")
    print(f"Diferencia: ${abs(diferencia):,.0f} ({estado})")
    
    # 7. Gráficos
    graficar_gastos_categoria(gastos_cat)
    graficar_comparativa_presupuesto(presupuesto, total_mes)
    
    print("\n✅ Análisis completo. Revisa las gráficas que se abrieron.")

if __name__ == "__main__":
    main()