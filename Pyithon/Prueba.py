#!/usr/bin/env python


def main(args):
	contador=0
	b=0
	while contador <5:
		contador = contador +1
		print("Lleva ",contador,"numeros introducidos")
		a=int(input())
		b+=a
		print(b)
	print(b/5)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
