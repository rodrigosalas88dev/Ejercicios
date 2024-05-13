
print("BIENVENIDOS AL PROGRAMA LISTA DE LA COMPRA\n"
      "------------------------------------------\n")

lista_compra = []
input_usuario = None

while input_usuario != "Q":
    input_usuario = input("Que deseas agregar a la lista (Q) para salir?")
    if input_usuario == "Q":
        pass
    elif input_usuario in lista_compra:
        print("Esto ya esta en la lista")
        print(lista_compra)
    elif input_usuario not in lista_compra:
        if input(f"Seguro deseas agregar {input_usuario} a la lista de la compra?") == "S":
            lista_compra.append(input_usuario)
            print(lista_compra)

print(f"la lista de la compra es {lista_compra}")
