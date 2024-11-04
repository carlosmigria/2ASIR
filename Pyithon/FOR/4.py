#!/usr/bin/env python
#Diseñar un algoritmos que pida el inicio y el fin de una serie y muestre su suma.

def main(args):
	inicio=(int(input("Introduce el inicio de la serie: ")))
	Final=(int(input("Introduce el final de la serie: ")))
	suma=0
	for numero in range(inicio,Final):
			suma=suma + numero
	print(suma)
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
