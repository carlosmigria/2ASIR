#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    lista= open("archivo.txt", "w")
    lista.writelines(["fran hola","pedro hola"])
    lista.close()
    lista = open("archivo.txt", "r")
    print(lista.read())
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
