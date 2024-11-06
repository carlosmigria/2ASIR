#!/usr/bin/env python


def main(args):
    from operator import itemgetter
    from decimal import Decimal
    lista1=[('mates',Decimal('10')),('lengua',Decimal('0')),('historia',Decimal('8')),('ingles',Decimal('5')),('tecnologia',Decimal('7'))]
    milistaordenada=sorted(lista1,key=itemgetter(1))    
    print("ASIGNATURAS--Notas")
    print("=======================")
    for i in range(5):
         print(milistaordenada[i][0],"-----",milistaordenada[i][1])
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
