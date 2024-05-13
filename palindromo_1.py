
def es_palindromo():  # palindromo: palabra que al revez es igual
    texto = input("introduce un texto: ")
    texto_sin_espacios = texto.replace(" ", "")  # quitamos espacios al texto
    print(texto_sin_espacios)
    if texto_sin_espacios == "".join(reversed(texto_sin_espacios)):  # muestra el texto al revez
        print("correcto")
    elif texto_sin_espacios != "".join(reversed(texto_sin_espacios)):
        print("incorrecto")


es_palindromo()
