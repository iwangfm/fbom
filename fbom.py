#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import random

cpnt={}
skip=[1,1,1,1,1,1,1,1,1,1,2,2,2,3,3,4,1,1,1,1,1,1,1,1,1,1]

def main():
    if len(sys.argv)>1 :
        infile = sys.argv[1]
    else :
        infile = "demo.csv"

    try:
        f = open(infile)
    except:
        print "Open file '%s' error !!"%infile
        exit()

    try:
        outfile = open(sys.argv[2],"w+")
    except:
        outfile=open("out.csv","w+")

    print "symbol,number,place"
    outfile.write("symbol,number,place\n")

    for line in f.readlines():
        m,n=line.split(",")
        n=eval(n)

        k = cpnt[m] if cpnt.has_key(m) else 1

        print "%s,%d,"%(m,n),
        outfile.write("%s,%d,"%(m,n))

        for i in range(n):
            k += skip[random.randint(0,len(skip)-1)]
            sys.stdout.write("%s%d "%(m,k))
            outfile.write("%s%d "%(m,k))
        print
        outfile.write("\n")
        cpnt.update({m: k})
    print cpnt
    f.close()
    outfile.close()

if __name__ == '__main__':
    main()