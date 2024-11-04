#!/usr/bin/env python


def main(args):
    tupla1=('mates','10')
    tupla2=('lengua','0')
    tupla3=('historia','8')
    tupla4=('ingles','5')
    tupla5=('tecnologia','7')
    print("ASIGNATURAS INTODUCIDAS")
    lista1=[tupla1,tupla2,tupla3,tupla4,tupla5]
    lista1.sort()

    print(lista1)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
