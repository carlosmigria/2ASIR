#!/usr/bin/env python
from decimal import Decimal as D

def introduceDatos(listaalumno):
    for i in range(2):
        lista = []
        Alumno = input("Alumno: ")
        Nombre = input("Nombre: ")
        lista.append((Alumno, Nombre))
        
        total_notas = D(0)
        num_asignaturas = 2 
        
        for x in range(num_asignaturas):
            Asignatura = input("Asignatura: ")
            nota = D(input("Notas: "))
            lista.append((Asignatura, nota))
            total_notas += nota
        
        media = total_notas / num_asignaturas
        lista.append(("Media", media))  
        listaalumno.append(lista)
    
    return listaalumno

def ordenado(milista):
    milistaordenada = sorted(milista, key=lambda x: x[0][1])
    return milistaordenada

def mostrar(milistaordenada):   
    print("ASIGNATURAS -- Notas")
    print("=======================")
    for alumno in milistaordenada:
        print("\nAlumno:", alumno[0][0])
        print("Nombre:", alumno[0][1])
        for asignatura, nota in alumno[1:-1]:
            print(asignatura, "-----", nota)
        print("Media del Alumno:", alumno[-1][1])

def calcular_media_general(milista):
    total_media = sum(alumno[-1][1] for alumno in milista)
    media_general = total_media / len(milista)
    return media_general

def main(args):
    milista = [] 
    milista = introduceDatos(milista)
    milistaordenada = ordenado(milista)
    mostrar(milistaordenada)
    media_general = calcular_media_general(milista)
    print("Media General de todos los alumnos:", media_general)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
