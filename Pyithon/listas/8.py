#!/usr/bin/env python
def introduceDatos(listaalumno):
    from decimal import Decimal as D
    for i in range(2):
         lista=[]
         Alumno=input("Alumno: " )
         Nombre=input("Nombre: " )
         lista.append((Alumno,Nombre))
         for x in range(2):
              Asignatura=input("Asignatura: " )
              nota=input("Notas: " )
              lista.append((Asignatura,D(nota)))
                  
    return listaalumno

def ordenado(milista):
    from operator import itemgetter
    
    milistaordenada=sorted(milistaalumno,key=itemgetter(1))    
    return milistaordenada
    
def mostrar(milistaordenada):   
    print("ASIGNATURAS--Notas")
    print("=======================")
    for i in range(2):
        print("Alumno: ",milistaordenada[i][1]) 
        print(milistaordenada[i][1],"-----",milistaordenada[i][3])

def main(args):
    
    milista=[] 
    milista=introduceDatos(milista)
    
    milistaordenada=ordenado(milistaalumno)
    mostrar(milistaordenada)
    print(milistaordenada)
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
