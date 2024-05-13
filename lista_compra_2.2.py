"""
Ejercicio 7: Lista de la compra

Crea una función que dada una lista de la compra definida
fuera de la función, permita al usuario añadir un nuevo
item asegurandose que no exista anteriormente en la lista.
"""

lista_predefinida = ["pan", "leche", "queso", "tomate"]

def lista():

    while True:
        input_usuario = input("Que desea agregar a la lista? (Q) para salir: ")

        if input_usuario == "Q":
            print(f"la lista de la compra es {lista_predefinida}")
            break

        elif input_usuario in lista_predefinida:
            print("Esto ya esta en la lista")

        elif input_usuario not in lista_predefinida:
            lista_predefinida.append(input_usuario)
            print("Agregado!")
            print(lista_predefinida)


if __name__ == "__main__":
    lista()
