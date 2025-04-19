"""
Programa que genera un listado de asistencia
Autor: Maria Lucia
Fecha: Septiembre 2024
Licencia: GNU GPL V3
"""

def ingresar_texto(mensaje):
    texto=input(mensaje)
    return texto

def ingresar_entero(mensaje):
    repetir = True
    while repetir:
        try:
            entero = int(input(mensaje))
            repetir = False
        except:
            print("No es una entrada valida para un numero entero")
    return entero


def ingresar_real(mensaje):
    repetir = True
    while repetir:
        try:
            real = float(input(mensaje))
            repetir = False
        except:
            print("No es una entrada valida para un numero real")
    return real


def ingresar_real_rango(mensaje, valor_minimo, valor_maximo):
    repetir = True
    while repetir:
        valor = ingresar_real(mensaje)
        if valor < valor_minimo or valor > valor_maximo:
            print(f"o esta en los rangos {valor_minimo} y {valor_maximo}")
        else:
            repetir = False
    return valor


def ingresar_entero_rango(mensaje, valor_minimo, valor_maximo):
    repetir = True
    while repetir:
        valor = ingresar_entero(mensaje)
        if valor < valor_minimo or valor > valor_maximo:
            print(f"No esta en los rangos {valor_minimo} y {valor_maximo}")
        else:
            repetir = False
    return valor


def ingresar_entero_mayor_que(mensaje, valor_minimo):
    repetir = True
    while repetir:
        valor = ingresar_entero(mensaje)
        if valor <= valor_minimo:
            print(f"El  valor no es mayor que {valor_minimo}")
        else:
            repetir = False
    return valor


def ingresar_real_mayor_que(mensaje, valor_minimo):
    repetir = True
    while repetir:
        valor = ingresar_real(mensaje)
        if valor <= valor_minimo:
            print(f"El  valor no es mayor que {valor_minimo}")
        else:
            repetir = False
    return valor


def mostrar_mensaje(mensaje):
    print(mensaje)


def generar_mensaje_tabla_multiplicar(numero_tabla, minimo_valor, maximo_valor):
    mensaje_tabla = f"\n TABLA DE MULTIPLICAR DEL {numero_tabla}\n\n"
    i = minimo_valor
    while i <= maximo_valor:
        producto = numero_tabla * i
        mensaje_tabla += f"{numero_tabla:2d} x {i:2d} = {producto:3d}\n"
        i = i + 1
    return mensaje_tabla

def verificar_es_vocal(letra):
    es_vocal =letra.lower() in "aeiou"
    return es_vocal

def ingresar_texto_longitud(mensaje, longitud):
    repetir = True
    while repetir:
        texto = ingresar_texto(mensaje)
        if len(texto) != longitud:
            print(f"El número no tiene una longitud de {longitud}")
        else:
            repetir = False
    return texto

def ingresar_mensaje_lista(mensaje, lista):
    repetir = True
    while repetir:
        texto= input(mensaje)
        if texto in lista:
            repetir = False
        else:
            print("lo que pusiste no està dentro de las opciones, intenta de nuevo: ")
    return texto