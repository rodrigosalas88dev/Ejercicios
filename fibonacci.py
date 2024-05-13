"""
Ejercicio 1: La secuencia de Fibonacci
Crea una función recursiva que devuelva una posición concreta de la secuencia de fibonacci
De esa manera mostraríamos la secuencia de fibonacci de la siguiente manera:

for f in range(8):
    print(fibonacci(f))
>1
1
2
3
5
8
13

Ejercicio 2: La secuencia de Fibonacci... Sin recursividad
La secuencia de Fibonacci se puede resolver también sin usar la recursividad,
¿Puedes averiguar cómo? Ya sabes... google.com es tu amigo,
implementa un programa en Python que muestre la secuencia de Fibonacci sin usar recursividad.

Ejercicio 3: Potencia con parámetro opcional
Crea una función para calcular la potencia de un número,
la función tendrá un parametro opcional que será la base de la potencia,
si no se especifica ninguna base, la base será 2. Ejemplo:

potencia(2)
> 4
potencia(2, 2)
> 4
potencia(2, 4)
> 16
potencia(3, 9)
> 19683
"""

#  a + b = c + b = d + c

# F(0)=0
# F(1)=1
# F(n)=F(n−1)+F(n−2) para 2 n≥2

# F(1)=0
# F(2)=1
# F(3)=1
# F(4)=2
# F(5)=3
# F(6)=5
# F(7)=8
# F(8)=13
"""
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
"""


def fibonacci(f):
    if f <= 1:
        return f
    a, b = 0, 1
    for n in range(2, f + 1):
        a, b = b, a + b
        print(b)
    return b


def main():
    (fibonacci(8))


if __name__ == "__main__":
    main()
