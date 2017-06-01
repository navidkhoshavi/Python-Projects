__author__ = 'Navid Khoshavi'

import sys
import re
from inspect import currentframe


# access type = 0 = read
# access type = 1 = write
# access type = 2 = update
# access type = 3 = evict
# access type = 4 = prefetch
# access type = 5 = insert (MEM writes LLC) when LLC has a read miss
# access type = 6 = writeback (LLC writes MEM)

CL1 = 0
CL2 = 0
WC = 0
totalWC = 0
flag = 1
with open('llc_access_trace_sorted.log', 'r') as ftrace:
    for line in ftrace:
        CL1 = int(line.split()[2])
        if CL1 == CL2 or flag==1:
            if int(line.split()[1]) == 1 or int(line.split()[1]) == 3:
                WC += 1
                flag = 0
                if WC > 7:
                    totalWC += 1
            CL2 = int(line.split()[2])
        else:
            WC = 0
            flag = 1

              
fout = open('totalWC',"w") 
print >>fout, "The number of Total Write operations are:", totalWC
fout.close()		






