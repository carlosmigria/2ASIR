#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("num" ,type=int)
    args = parser.parse_args()
    print(args.num*args.num)
    
    
   
    sys.exit(main(sys.argv))
