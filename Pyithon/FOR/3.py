#!/usr/bin/env python
#Diseñar un algoritmo que pida el inicio y el fin de una serie y la muestre.

def main(args):
	inicio=(int(input("Introduce el inicio de la serie: ")))
	Final=(int(input("Introduce el final de la serie: ")))
	for numero in range(inicio,Final):
		print(numero)
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
