#!/usr/bin/env python
from decimal import Decimal as D

def introduceDatos(listaalumno):
    for i in range(2):  # Cambia 2 por el número de alumnos que desees
        lista = []
        Alumno = input("Alumno: ")
        Nombre = input("Nombre: ")
        lista.append((Alumno, Nombre))
        
        total_notas = D(0)
        num_asignaturas = 2  # Cambia a la cantidad de asignaturas por alumno
        
        for x in range(num_asignaturas):
            Asignatura = input("Asignatura: ")
            nota = D(input("Notas: "))
            lista.append((Asignatura, nota))
            total_notas += nota
        
        media = total_notas / num_asignaturas
        lista.append(("Media", media))  # Añadimos la media de cada alumno
        listaalumno.append(lista)
    
    return listaalumno

def ordenado(milista):
    # Ordenamos la lista por el nombre del alumno (index [0][1])
    milistaordenada = sorted(milista, key=lambda x: x[0][1])
    return milistaordenada

def mostrar(milistaordenada):   
    print("ASIGNATURAS -- Notas")
    print("=======================")
    for alumno in milistaordenada:
        print("\nAlumno:", alumno[0][0])
        print("Nombre:", alumno[0][1])
        for asignatura, nota in alumno[1:-1]:  # Excluye la última entrada (media)
            print(asignatura, "-----", nota)
        print("Media del Alumno:", alumno[-1][1])  # La última entrada es la media

def calcular_media_general(milista):
    total_media = sum(alumno[-1][1] for alumno in milista)  # Suma las medias de cada alumno
    media_general = total_media / len(milista)
    return media_general

def main(args):
    milista = [] 
    milista = introduceDatos(milista)
    milistaordenada = ordenado(milista)
    mostrar(milistaordenada)
    
    media_general = calcular_media_general(milista)
    print("\nMedia General de todos los alumnos:", media_general)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
