#!/usr/bin/env python
#Diseñar un algoritmo que muestra el factorial de un número pedido al usuario. El número
#debe ser mayor de 0
def main(args):
	n=(int(input("Introduce el numero que quieres que se le haga el factorial: ")))
	i=1
	for numero in range(1,n+1):
		i= i * numero
	print(i)
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
