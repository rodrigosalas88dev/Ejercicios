"""
Ejercicio 4: Pregunta algo

Crea una función que pregunte al usuario si esta seguro o no,
 y devuelva los valores "True" o "False"
  dependiendo de si el usuario está seguro.
"""

def seguro():
    while True:
        pregunta = input("Estas Seguro? S/N: ")

        if pregunta == "S":
            print(pregunta == "S")
            break
        elif pregunta == "N":
            print(pregunta != "N")
            break
        else:
            pass


if __name__ == "__main__":
    seguro()
