"""
Ejercicio 6: Adivina el número

Crea una función que reciba como argumento un número
del 1 al 100 a adivinar y que le pregunte al usuario que
adivine el número. El código se ejecutará hasta que el
usuario adivine.

"""


def adivina(numero):

    while True:
        input_usuario = input("Adivina el numero de 1 al 100: ")
        if input_usuario != str:
            print("Tecla incorrecta")

        elif int(input_usuario) == numero:
            print("Has acertado!")
            break

        elif int(input_usuario) != numero:
            print("No acertaste")


if __name__ == "__main__":
    adivina(19)
