"""
Programa que almacena 5 nombres en una lista y los muestra en orden inverso
"""

def main():
    nombres = ingresar_nombres()
    mensaje = generar_mensaje(nombres)
    mostrar_mensaje(mensaje)

def ingresar_nombres():
    nombres = []
    for i in range(5):
        nombre = input(f"Ingrese el nombre {i+1}: ")
        nombres.append(nombre)
    return nombres

def generar_mensaje(nombres):
    mensaje = "Los nombres ingresados en orden inverso son:\n"
    for nombre in reversed(nombres):
        mensaje += f"{nombre}\n"
    return mensaje

def mostrar_mensaje(mensaje):
    print(mensaje)

main()