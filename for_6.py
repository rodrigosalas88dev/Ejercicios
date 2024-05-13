
input_usuario = int(input("Que numero deseas multiplicar?: "))

for n in range(1, 11):
    if n % 2 == 0: #(modulo %, es lo que sobra de una division, si da 0 es que es divisible y la division no tiene resto)
        print(f"{n} x {input_usuario} = {n * input_usuario}")