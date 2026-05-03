# entrada_presupuesto.py
# Pide el presupuesto al usuario y lo devuelve como número

def pedir_presupuesto():
    """
    Solicita al usuario el presupuesto mensual.
    Repite hasta que ingrese un número válido y no negativo.
    """
    while True:
        try:
            valor = float(input("Ingresa tu presupuesto mensual(sin comas ni puntos): $"))
            if valor < 0:
                print("El presupuesto no puede ser negativo. Intenta de nuevo.")
            else:
                return valor
        except ValueError:
            print("Debes ingresar un número (ejemplo: 200000).")