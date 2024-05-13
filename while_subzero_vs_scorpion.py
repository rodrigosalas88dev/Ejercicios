
from random import randint
import os

VIDA_INICIAL_SCORPION = 90
VIDA_INICIAL_SUBZERO = 90

vida_scorpion = VIDA_INICIAL_SCORPION
vida_subzero = VIDA_INICIAL_SUBZERO


while vida_subzero > 0 and vida_scorpion > 0:
    print("El combate continua")
    print("Ataca Subzero")

    ataque_subzero = randint(1, 2)

    if ataque_subzero == 1:
        print("Subzero ataca con Patada Alta")
        vida_scorpion -= 10
    elif ataque_subzero == 2:
        print("Subzero ataca con Congelar")
        vida_scorpion -= 12

    if vida_scorpion <= 0:
        vida_scorpion = 0
        print("Scorpion ha muerto")
        exit()

    if vida_subzero <= 0:
        vida_subzero = 0
        print("Subzero ha muerto")
        exit()

    porecentaje_scorpion = int(vida_scorpion * 100 / VIDA_INICIAL_SCORPION)
    porcentaje_subzero = int(vida_subzero * 100 / VIDA_INICIAL_SUBZERO)

    print("La vida de Scorpion es: [{}{}] ({}%)".format(porecentaje_scorpion * "*", " " * 10, porecentaje_scorpion))
    print("La vida de Subzero es: [{}{}] ({}%)".format(vida_subzero * "*", " " * VIDA_INICIAL_SUBZERO, porcentaje_subzero))

    input("Enter para continuar")
    os.system("cls")

    ataque_scorpion = input("¿Que ataque eliges? Gancho (A) o Infierno (B)")

    if ataque_scorpion == "A":
        print("Scorpion ataca con Gancho")
        vida_subzero -= 10
    elif ataque_scorpion == "B":
        print("Scorpion ataca con Infierno")
        vida_subzero -= 12
    else:
        while ataque_scorpion != "A" and ataque_scorpion != "B":
            print("Debes elejir un ataque")
            ataque_scorpion = input("¿Que ataque eliges? Gancho (A) o Infierno (B)")

            if ataque_scorpion == "A":
                print("Scorpion ataca con Gancho")
                vida_subzero -= 10
            elif ataque_scorpion == "B":
                print("Scorpion ataca con Infierno")
                vida_subzero -= 12

    tamano_barra_vida_s = int(vida_scorpion * 10 / VIDA_INICIAL_SCORPION)
    tamano_barra_vida_sub = int(vida_subzero * 10 / VIDA_INICIAL_SUBZERO)

    print("La vida de Scorpion es: [{}] ({}%)".format(tamano_barra_vida_s, vida_scorpion))
    print("La vida de Subzero es: [{}] ({}%)".format(tamano_barra_vida_sub, vida_subzero))

    input("Enter para continuar")
    os.system("cls")
