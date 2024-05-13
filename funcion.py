"""
Ejercicio 1

Usando la nueva estructura de programas basado en la función main() y la condición if final,
crea un programa de cualquier tipo. Lo que te de la gana. Usa el debugger para ver como se
produce el hilo de ejecución del código.

Ejercicio 2

Crea un programa que contenga una función que calcule la potencia de un numero introducido
 como argumento, por ejemplo:

print(potencia(3))
> 9
print(potencia(5))
> 25

"""


if __name__ == "__main__":
    def main():
        saludo = "hola mundo"
        print(saludo)


    main()

    def potencia(numero):
        n = numero * numero
        print(n)


    potencia(3)
