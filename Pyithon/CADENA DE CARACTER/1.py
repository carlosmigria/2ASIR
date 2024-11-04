#!/usr/bin/env python


def main(args):
	cadena=input("Introduzca la frase: ")
	cadena1=cadena
	print("HECHO CON RANGE")
	for a in range(len(cadena)):
		print(cadena[a]) 
	print("HECHO USANDO LA CARACTERSTICA ITERABLES DE LAS CADENAS")
	for letra in cadena1:
		print(letra)
	return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
