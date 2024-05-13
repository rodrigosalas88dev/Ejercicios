"""
Ejercicio 5: A mayus

Crea una función que convierta toda una string en mayusculas, no vale usar el método upper()
"""

"""
def convierte_a_mayus():
    cadena = input("Ingresa una cadena: ")
    cadena_mayus = ""
    for char in cadena:
        if 'a' <= char <= 'z':
            # Convertir el caracter a mayúscula sumándole la diferencia entre 'a' y 'A'
            char = chr(ord(char) - ord('a') + ord('A'))
        cadena_mayus += char
    print("Palabra en mayúsculas: {}".format(cadena_mayus))
    return cadena_mayus
"""

def mayusculas():
    texto = input("Ingresa un texto: ")
    texto_mayuscula = ""
    for char in texto:
        if "a" <= char <= "z":
            char = chr(ord(char) - ord("a") + ord("A"))
        texto_mayuscula += char
    print(f"Palabra en mayusculas: {texto_mayuscula}")
    return texto_mayuscula


if __name__ == "__main__":
    mayusculas()
