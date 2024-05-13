import os

lista = []

seleccion = None

print("BIENVENIDO AL PROGRAMA LISTA DE LA COMPRA\n"
      "-----------------------------------------\n\n")

while True:
    seleccion = input("¿Que desea comprar? (Q) para salir: ")
    if seleccion == "Q":
        break
    elif seleccion in lista:
        print("{} ya está en la lista!".format(seleccion))
    elif input("Seguro deseas añadir {} en la lista? (S/N): ".format(seleccion)) == "S":
        lista.append(seleccion)
    else:
        print("Ok, no agregamos nada!")

print("La lista de la compra es: {}".format(lista))

print("Presione Enter para continuar")
os.system("cls")

while True:
    seleccion = input("Desea quitar algo de la lista? Indiquelo o (Q) para salir: ")
    if seleccion == "Q":
        break
    elif input("Seguro deseas quitar {} de la lista? (S/N) ".format(seleccion)) == "S":
        if seleccion in lista:
            lista.remove(seleccion)
        else:
            print("Esto no esta en la lista")
    else:
        break

print("La lista de la compra es: {}".format(lista))

print("Presione Enter para continuar")
os.system("cls")


