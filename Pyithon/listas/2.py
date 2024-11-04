#!/usr/bin/env python


def main(args):
    primera=input("Dame la asigantura 1: ")
    segunda=input("Dame la asigantura 2: ")
    tercera=input("Dame la asigantura 3: ")
    cuarta=input("Dame la asigantura 4: ")
    quinta=input("Dame la asigantura 5: ")
    a=[primera,segunda,tercera,cuarta,quinta]
    a.sort()
    print(a)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
