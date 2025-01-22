#!/usr/bin/env python
# -*- coding: utf-8 -*-
def muestradatos(referencia,precio):
    print(referencia)
    print(precio)
def main(args):
    muestradatos(referencia='AA123',precio=2.54)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
