#!/usr/bin/env python
# -*- coding: utf-8 -*-
def mostrarDatos(diccionario):
    for servidor in diccionario:
        print (f" {servidor}")
        for clave,valor in diccionario[servidor].items():
            if clave != "DNS":
                print(f"\t{clave}---->{valor}")
            else:
                print(f"\tDNS:")
                for p in valor:
                    print(f"\t{p}")
def introducirDatos():
    Bdatos1={}
    s = int(input("Intoduce el numero de servidores que quieras dar de alta:"))
    for i in range(s):
        NServer=input("Introduce el nombre del servidor:")
        ip=input("Introduce la ip del servidor:")
        masc=input("Introduce la masc servidor:")
        gateway=input("Introduce la gateway servidor:")
        NDNS=int(input("Introduce el numero de DNS que quieres ponerle al servidor:"))
        for i in range(NDNS):
            DNS=input("Introduce el nombre del servidor:")
            Bdatos1.update({NServer:{"ip:": ip,"masc: ": masc,"gateway:": gateway,"DNS: ": DNS,}})
    return Bdatos1

def main(args):
    
    datos=introducirDatos()
    print(datos)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
