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
    fran={}
    s = int(input("Intoduce el numero de servidores que quieras dar de alta:"))
    for i in range(s):
        NServer=input("Introduce el nombre del servidor:")
        ip=input("Introduce la ip del servidor:")
        masc=input("Introduce la masc servidor:")
        gatewayu=input("Introduce la masc servidor:")
        NDNS=int(input("Introduce el numero de DNS que quieres ponerle al servidor:"))
        for i in range(NDNS):
            DNS=input("Introduce el nombre del servidor:")
            fran.update({NServer:{"ip:": ip,"masc: ": masc,"DNS: ": DNS,}})
    return fran

def main(args):
    
    datos= {
           'Serv1':{
                   "ip":"192.168.8.1",
                   "masc":"255.255.255.0",
                   "gateway":"192.168.8.1",
                   "DNS":["1.1.1.1","8.8.8.8"]
                   },
           'Serv2':{
                   "ip":"192.168.8.2",
                   "masc":"255.255.255.0",
                   "gateway":"192.168.8.1",
                   "DNS":["1.1.1.1","8.8.8.8"]
                   }
            }
    fran=introducirDatos()
    print(fran)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
