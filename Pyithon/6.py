#!/usr/bin/env python


def main(args):
	num1=int(input("Ponga el primero numero "))
	num2=int(input("Ponga el segundo numero "))
	num3=int(input("Ponga el tercer numero "))
	num4=int(input("Ponga el cuarto numero "))
	num5=int(input("Ponga el quinto numero "))
	suma1=num1+num2+num3+num4+num5
	resultado=suma1/5
	print(resultado)
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
