import string

texto_usuario = input("Introduzca un texto: ")
mayusculas = 0

for letra in texto_usuario:
    if letra in string.ascii_uppercase:
        mayusculas += 1

print(f"mayusculas: {mayusculas}")
