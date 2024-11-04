#!/usr/bin/env python
# Diseñar un algoritmo que muestre la suma de los pares que hay entre un inicio y un final
#definidos por el usuario

def main(args):
	inicio=(int(input("Introduce el inicio de la serie: ")))
	Final=(int(input("Introduce el final de la serie: ")))
	suma=0
	for numero in range(inicio,Final):
		resultado = numero % 2 
		if resultado == 0:
			suma=suma + numero
	print(suma)
			
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
