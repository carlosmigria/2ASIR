#!/usr/bin/env python
def introduceDatos(lista):
    from decimal import Decimal as D
    for i in range(5):
         print ("ASIGNATURA",i+1)
         Nombre=input("Nombre: " )
         nota=input("Notas: " )
         
         lista.append((Nombre,D(nota)))
    return lista
    
def ordenado(milista):
    from operator import itemgetter
    
    milistaordenada=sorted(milista,key=itemgetter(1))    
    return milistaordenada
    
def mostrar(milistaordenada):   
    print("ASIGNATURAS--Notas")
    print("=======================")
    for i in range(5):
        print(milistaordenada[i][0],"-----",milistaordenada[i][1])   
             
def main(args):
    
    milista=[] 
    milista=introduceDatos(milista)
    
    milistaordenada=ordenado(milista)
    mostrar(milistaordenada)
    print(milistaordenada)
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
