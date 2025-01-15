#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import re

def es_correo_electronico(cadena):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, cadena))

# Ejemplo de uso
print(es_correo_electronico("correo@ejemplo.com"))  # True
print(es_correo_electronico("no_es_correo"))       # False

def main(args):
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
