"""
Programa que genera una tabla de multiplicar
"""
from apoyo import ingresar_entero_rango, mostrar_mensaje

MINIMO_TABLA = 0
MAXIMO_TABLA = 10
VALOR_MINIMO = 0
VALOR_MAXIMO = 20


def main():
    numero_tabla = ingresar_entero_rango("Ingrese el numero de la tabla: ", VALOR_MINIMO, VALOR_MAXIMO)
    mensaje = generar_mensaje_tabla_multiplicar(numero_tabla, MINIMO_TABLA, MAXIMO_TABLA)
    mostrar_mensaje(mensaje)


def generar_mensaje_tabla_multiplicar(numero_tabla, minimo_valor, maximo_valor):
    mensaje_tabla = f"\n TABLA DE MULTIPLICAR DEL {numero_tabla}\n\n"
    i = minimo_valor
    while i <= maximo_valor:
        producto = numero_tabla * i
        mensaje_tabla += f"{numero_tabla:2d} x {i:2d} = {producto:3d}\n"
        i = i + 1
    return mensaje_tabla


main()
