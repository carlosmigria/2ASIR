#!/usr/bin/env python
def main(args):
	cadena = input("Introduzca la frase: ")
	b = input("Introduce la letra: ")
	contador = 0
	for a in range(len(cadena)):
		if cadena[a] == b:
			contador = contador +1
	print (contador)
	return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
