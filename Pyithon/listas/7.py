#!/usr/bin/env python
def introduceDatos(lista):
    from decimal import Decimal as D
    for i in range(3):
       print("Alumno", i)
       for a in range(2):
          print("Asignatura", a+1)
          nombreA=input("Nombre de la asignatuira: ")
          nota=input("Nota de la asignatuira: ")
          lista.append((nombreA,D(nota)))
    return lista
def mostra(milista):
    print("ASIGNATURAS")
    print("===============")
    m=0
    for x in range(3):
        print("ALUMNO",x)
        for m in range(2):
            print(milista[m][0],"-----",milista[m][1])


def main(args):
    milista=[] 
    milista=introduceDatos(milista)
    mostra(milista)
    print (milista)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
