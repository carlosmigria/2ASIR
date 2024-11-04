#!/usr/bin/env python


def main(args):
    from operator import itemgetter
    from decimal import Decimal
    tupla1=('mates',Decimal('10'))
    tupla2=('lengua',Decimal('0'))
    tupla3=('historia',Decimal('8'))
    tupla4=('ingles',Decimal('5'))
    tupla5=('tecnologia',Decimal('7'))
    lista1=[tupla1,tupla2,tupla3,tupla4,tupla5]
    milistaordenada=sorted(lista1,key=itemgetter(1))
    print("ASIGNATURAS--Notas")
    print("=======================")
    for i and i<=5:
        
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
