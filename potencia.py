""" CREAR UNA FUNCION QUE CALCULE LA POTENCIA
DE UN NUMERO QUE LE PASEMOS Y
LA BASE DE LA POTENCIA ES EL SEGUNDO ARGUMENTO

potencia (4, 7) = 4 elevado a 7
potencia (4) = 4 elevado a 2



def potencia(numero, base=2)
    resultado = numero
    for a in range(1, base):
        reultado *= numero
    return resultado




"""


def potencia(int, *args):
    a = int * int
    print(a)
    for n in args:
        b = int ** n
        print(b)
        return a, b


def main():
    potencia(8)
    potencia(4, 5)


if __name__ == "__main__":
    main()
