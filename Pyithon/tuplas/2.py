#!/usr/bin/env python
def menu():
		print("0.salir")
		print("1.Suma")
		print("2.Resta")
		print("3.Division")
		print("4.multiplicacion")
		op = int(input("introduce la operacion que quiere realizar: "))	
		return op

def main(args):
	n1 = int(input("Introduce el primer numero: "))
	n2 = int(input("Introduce el segundo numero: "))
	op = menu()
	while op<0 or op>4:
		print("El numero introducido en el menu no esta dentro del parametro: ")
		op = menu()
	if op == 1:
		suma = n1 + n2
		print("El resultado de",n1,"mas ",n2,"es",suma,)
		op = menu()
	elif op == 2:
		resta = n1 - n2
		print("El resultado de",n1,"menos",n2,"es",resta,)
		op = menu()
	elif op == 3:
		division = n1 / n2
		print("El resultado de",n1,"entre",n2,"es",division,)
		op = menu()
	elif op == 4:
		multiplicacion = n1 * n2
		print("El resultado de",n1,"por",n2,"es",multiplicacion,)
		op = menu()
	else:
		print ("Saliendo del programa")
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
