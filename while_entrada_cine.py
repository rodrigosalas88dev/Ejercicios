#bebes entran gratis menores de 5 años
#niños de 5 a 18 pagan 5 euros
#personas de 18 a 55 pagan 10
#mayores de 55 pagan con descuento

print("BIENVENIDO AL DESCUENTO PARA EL CINE\n"
      "------------------------------------\n")

edad = -1

while edad == -1:
    int(input("Introduce la edad para ver el precio: "))
    if edad != -1:
        break

if edad < 5 and edad >0:
    print("Este niño entra gratis")

elif edad >= 5 and edad < 18:
    print("Te corresponde pagar €5 de entrada")

elif edad >= 18 and edad < 55:
    print("Te corresponde pagar €10 de entrada")

elif edad >= 55:
    print("Entras con descuento")
