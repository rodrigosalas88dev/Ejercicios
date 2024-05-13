"""
Ejercicio 3: Par o impar

Crea una función que te de True como resultado si el número pasado como argumento es impar

Ejemplo:

es_impar(3)

> True

es_impar(24)

> False
"""


def impar(numero):

    if numero % 2 != 0:
        print(f"Es impar ({numero})")
        numero = True
        print(numero)

    else:
        print(f"Es par ({numero})")
        numero = False
        print(numero)


if __name__ == "__main__":
    impar(8)
