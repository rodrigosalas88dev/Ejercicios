"""
# espacios = 6
# puntos = 1
# comas = 1
HOLA, ME LLAMO RODRIGO. SOY DESARROLADOR JUNIOR Y ESTOY TELETRABAJANDO.
"""
texto_usuario = None

espacios = " "
numero_espacios = 0
comas = ","
numero_comas = 0
puntos = "."
numero_puntos = 0

while texto_usuario != "Q":
    texto_usuario = input("Introduce el texto a contar, (Q) para salir: ")
    print(texto_usuario)
    pass
    if texto_usuario == "Q":
        print("Has salido del programa")
        exit()
    for letra in texto_usuario:
        if letra in comas:
            numero_comas += 1
            print(f"Hay {numero_comas} ({comas}) en {texto_usuario}")
        elif letra in puntos:
            numero_puntos += 1
            print(f"Hay {numero_puntos} ({puntos}) en {texto_usuario}")
        elif letra in espacios:
            numero_espacios += 1
            print(f"Hay {numero_espacios} ({espacios}) en {texto_usuario}")

print(f"Hay {numero_comas} ({comas}) en total en la frase")
print(f"Hay {numero_puntos} ({puntos}) en total en la frase")
print(f"Hay {numero_espacios} ({espacios}) en total en la frase")

"""
OTRA MANERA DE HACERLO ES:

texto_usuario = input("introduzca un texto")
espacios = 0
comas = 0
puntos = 0

for letra in texto_usuario
    if letra == " ":
        espacios += 1
    elif letra == ",":
        comas += 1
    elif letra == ".":
        puntos += 1
        
print("Espacios: {}, Puntos: {}, Comas {}".format(espacios, puntos, comas))

"""