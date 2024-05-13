"""
Ejercicio 2: Sumando la lista

Crea una función que sume una lista de números, no se vale usar la función sum()

Ejemplo:

suma([1, 2, 3, 4, 5])

> 15
"""

def sumando(numero):
    lista = 0
    for n in numero:
        lista += int(n)
    print(lista)


if __name__ == "__main__":
    sumando([3, 3, 3])
