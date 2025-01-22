#!/usr/bin/env python
# -*- coding: utf-8 -*-
def suma(*args):
    resultado = 0
    for argumento in args:
        resultado += argumento
    return resultado


def main(args):
    print(suma(1,2))
    print(suma(3,4,5))
    print(suma(4,5,1,7))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
