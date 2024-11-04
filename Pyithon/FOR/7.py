#!/usr/bin/env python
#Diseñar un algoritmo que muestre la tabla de multiplicar de un número que pide al usuario y
#que debe estar entre 1 y 10 (ambos inclusive).
def main(args):
	tabla=(int(input("Porque tabla quieres multiplicar: ")))
	i=1
	for numero in range(11):
		i=numero*tabla
		print(i)
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
