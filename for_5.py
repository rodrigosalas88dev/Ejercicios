#CREAR TABLA DE MULTIPLICAR EN BASE AL NUMERO QUE DIGA EL USUARIO

input_usuario = int(input("Que numero deseas multiplicar?: "))

for n in range(1, 11):
    print(f"{input_usuario} x {n} = {input_usuario * n}")
