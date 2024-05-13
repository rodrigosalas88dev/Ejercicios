

lista_compra_establecida = ["tomate", "pollo", "leche", "cereales"]
lista_compra = []
ARCHIVO_LISTA = "lista_compra.txt"


def archivo():
    with open(ARCHIVO_LISTA, "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))


def cargar_lista():
    lista_compra = []
    if input("Te interesa cargar la ultima lista de la compra? (S/N): ") == "S":
        try:
            with open(ARCHIVO_LISTA, "r") as a:
                lista_compra = a.read().split("\n")
        except FileNotFoundError:
            print("Archivo no encontrado!")
    return lista_compra
    lista()



"""
a = open(ARCHIVO_LISTA, "w")
a.write("\n".join(lista_compra))
a.close()
return a
"""


def lista():

    while True:
        input_usuario = input("Que desea agregar a la lista?\n"
                              "(Q) para salir o (L) productos disponibles: ")

        if input_usuario.upper() == "Q":
            imprimir_lista()
            break

        elif input_usuario.upper() == "L":
            print(lista_compra_establecida)

        elif input_usuario.lower() in [a.lower() for a in lista_compra]:
            print("Esto ya esta en la lista")

        elif input_usuario.lower() not in [a.lower() for a in lista_compra_establecida]:
            print("Este producto no esta disponible para agregar en la lista")

        elif input_usuario.lower() not in [a.lower() for a in lista_compra] and input_usuario.lower() in [a.lower() for a in lista_compra_establecida]:
            lista_compra.append(input_usuario)
            print("Agregado!")
            imprimir_lista()


def imprimir_lista():
    print("\n".join(lista_compra))


def main():
    lista_compra = cargar_lista()
    imprimir_lista()
    lista()
    archivo()


if __name__ == "__main__":
    main()
