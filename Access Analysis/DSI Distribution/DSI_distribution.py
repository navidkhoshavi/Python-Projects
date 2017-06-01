__author__ = 'Navid Khoshavi'
import sys
import re

bin0_2M = 0
bin2M_4M = 0
bin4M_8M = 0
bin8M_16M = 0
bin16M_more = 0
fout = open("DSI_dist.log","w")
with open('DSI.log', 'r') as ftrace:
    for line in ftrace:
        if int(line.split()[3]) < 2000000:
            bin0_2M += 1
        elif int(line.split()[3]) < 4000000:
            bin2M_4M += 1
        elif int(line.split()[3]) < 8000000:
            bin4M_8M += 1
        elif int(line.split()[3]) < 16000000:
            bin8M_16M += 1
        else:
            bin16M_more += 1
    print >>fout, "%-9s %-9s %-9s %-9s %-9s" % (bin0_2M, bin2M_4M, bin4M_8M, bin8M_16M, bin16M_more)
fout.close()


# fix me: in the second elsif, I have to consider the previous Mem access