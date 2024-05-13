# HAY QUE BUSCAR VOCALES EN ESTA FRASE UTILIZANDO EL FOR:
# VOY A HACERME DESARROLLADOR Y TRABAJAR ANTES DE LOS 4 MESES

frase = "Voy a hacerme desarrollador y trabajar antes de los 4 meses"
vocales = ["a", "e", "i", "o", "u"]
numero_vocales = 0

for letra in frase: #el IN del FOR significa por cada letra que hay DENTRO de la frase
    if letra in vocales: #el IN del IF significa si la letra ESTA EN VOCALES , VERDADERO O FALSO, OPERACION BOOLEANA
        print(f"He encontrado una {letra}")
        numero_vocales += 1

print(f"Vocales encontradas {numero_vocales}")