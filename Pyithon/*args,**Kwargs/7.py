#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("datos",
                        type=int,
                        help="Dos números enteros de los que desea el cuadrado",
                        nargs=2)
    args = parser.parse_args()
    for numero in args.datos:
        print(numero * numero)
    sys.exit(main(sys.argv))

