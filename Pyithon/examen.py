#!/usr/bin/env python
def main(args):
    import random
    numero_secreto = random.randint(1,100)
    print(numero_secreto)
    contador = 1
    print ("MINI JUEGO PARA ADIVINAR UN NUMERO")
    numeroi = int(input("introduce un numero del 1 al 100:"))
    while numeroi != numero_secreto:
        print(contador)
        print(numero_secreto)
        contador = contador + 1
        if numeroi > numero_secreto:
            print ("el numero secreto es menor")
            numeroi = int(input("introduce un numero del 1 al 100:"))
        else:
            print ("el numero secreto es mayor")
            numeroi = int(input("introduce un numero del 1 al 100:"))
    print ("Feliciadades Has adivinado el numero en",contador,"intentos.")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
