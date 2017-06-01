__author__ = 'Navid Khoshavi'
import sys
import re




maxInterval = 0
CL = 0
fout = open("maxWrite2LastRead.log","w")
with open('avg2Write.log', 'r') as ftrace:
    for line in ftrace:
        for x in xrange(0, 8):
            if line.split()[3] != 0:
                tmp1 = line.split()[3]
                tmp2 = line.split()[0]
                if maxInterval < tmp1:
                    maxInterval = tmp1
                    CL = tmp2
            line = ftrace.next()
        print >>fout, "%-9s %-9s" % (CL, maxInterval)
        maxInterval = 0
        CL = 0

fout.close()


# fix me: in the second elsif, I have to consider the previous Mem access