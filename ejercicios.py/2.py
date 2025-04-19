"""
Encontar cual es el numero que mas se repite en una lista de numeros
"""

LISTA=[2,3,4,45,6,7,8,8,2,1,2,3,4,7,5,3,4,2,3,2,90]

def main():
    mayor_numero=determinar_numero(LISTA)
    mensaje=generar_mensaje(mayor_numero)
    mostar_mensaje(mensaje)

def determinar_numero(lista):
    if not lista:
        return None 

    max_repeticiones = 0
    mayor = lista[0]  

    for i in range(len(lista)):
        referencia = lista[i]
        contador = 0

       
        for j in range(len(lista)):
            if lista[j] == referencia:
                contador += 1

        if contador > max_repeticiones:
            max_repeticiones = contador
            mayor = referencia

    return mayor

def generar_mensaje(mayor):
    mensaje=f"El numero que mas se repite es {mayor} de la lista presentada"
    return mensaje

def mostar_mensaje(mensaje):
    print(mensaje)


main()
