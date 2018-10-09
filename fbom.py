#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import random

comp={}

def main():
    f = open(sys.argv[1])

    print "symbol,number,place"

    for line in f.readlines():
        m,n=line.split(",")
        n=eval(n)

        k = comp[m] if comp.has_key(m) else 1

        print "%s,%d,"%(m,n),

        for i in range(n):
            k += random.randint(1,3)
            sys.stdout.write("%s%d "%(m,k))
        print
        comp.update({m: k})
    print comp
    f.close()

if __name__ == '__main__':
    main()