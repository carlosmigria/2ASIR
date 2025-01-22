#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def muestradatos(**kwargs):
    for clave, valor in kwargs.items():
        print(clave, ":", valor)


def main(args):
    muestradatos(precio=2.54,referencia='AA123')
    muestradatos(referencia='BB234',precio=5.25,categoria='frutas')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
