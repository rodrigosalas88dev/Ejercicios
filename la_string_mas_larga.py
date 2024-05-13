"""
Ejercicio 1: La string más larga

Crea una funcion que reciba una lista de strings como entrada y te diga cual es la más larga de todas

Ejemplo:

string_mas_larga("hola", "como", "estas")

> "estas"

"""


def string_mas_larga(arg1, arg2, arg3):
    args = [arg1, arg2, arg3]
    print(args.count(arg3))
    print(max(len(arg1), len(arg2), len(arg3)))

    if len(arg1) < len(arg2):
        print(arg2)
    elif len(arg1) < len(arg3):
        print(arg3)
    else:
        print(arg1)


if __name__ == "__main__":
    string_mas_larga("hola", "como", "estas")
