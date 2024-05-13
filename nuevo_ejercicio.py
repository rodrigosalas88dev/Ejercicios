
input_usuario = None

lista_numeros = []

while input_usuario != "Q":

    input_usuario = input(
        "Que numero desea añadir a la lista, (Q) para salir: ")

    if input_usuario.upper() == "Q":
        break

    elif input("Seguro desea añadir este numero a la lista? (S) O (Q) para salir: ") == "S":
        lista_numeros.append(int(input_usuario))

try:
    print(f"La lista de numeros es: {lista_numeros}")
    print(f"El numero mas pequeño de la lista es {min(lista_numeros)}")
    print(f"El numero mas pequeño de la lista es {min(lista_numeros)}")
except ValueError:
    pass
