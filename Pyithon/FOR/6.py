#!/usr/bin/env python
#!/usr/bin/env python
#Diseñar un algoritmo que calcula la media de una serie de 10 números.

def main(args):
	inicio=(int(input("Introduce el inicio de la serie: ")))
	final=(int(input("Introduce el final de la serie: ")))
	suma=0
	for numero in range(inicio,Final):
			suma=suma + numero
			media = suma/final
	print(media)
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
