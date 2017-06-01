__author__ = 'Navid Khoshavi'
import sys
import re
import operator
import os

#Command to merge all files nvidia@ubuntu:~/simulation/gem5/m5out/TACO/$ cat /blackscholes/PhyAddr/addr/* > bk.BankTLB.out
with open('swaptions/PhyAddr/addr/swaptions.BankTLB.out', 'r') as fin:
        lines = [line.split() for line in fin]
        lines.sort(key=operator.itemgetter(0))

with open('swaptions/PhyAddr/addr/swaptions.BankTLB.out.sorted', 'w') as fout:
    for el in lines:
        fout.write('{0}\n'.format(' '.join(el)))
os.remove('swaptions/PhyAddr/addr/swaptions.BankTLB.out')



