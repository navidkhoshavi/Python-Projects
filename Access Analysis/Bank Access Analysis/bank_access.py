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


# find the largest CL number
def secondLargestCacheLine ():
    # find the largest CL number
    with open('llc_access_trace_sorted.log', 'r') as ftrace:
        largest = 0
    	for line in ftrace:
	    if (int(line.split()[2]) > largest):
                secondLargestCacheLine = largest
                largest = int(line.split()[2])              	
    return secondLargestCacheLine;



bank_partition = secondLargestCacheLine()/8;
with open('llc_access_trace_sorted.log', 'r') as ftrace:
    readCounterBank0 = 0
    readCounterBank1 = 0
    readCounterBank2 = 0
    readCounterBank3 = 0
    readCounterBank4 = 0
    readCounterBank5 = 0
    readCounterBank6 = 0
    readCounterBank7 = 0
    writeCounterBank0 = 0
    writeCounterBank1 = 0
    writeCounterBank2 = 0
    writeCounterBank3 = 0
    writeCounterBank4 = 0
    writeCounterBank5 = 0
    writeCounterBank6 = 0
    writeCounterBank7 = 0
    evictCounterBank0 = 0
    evictCounterBank1 = 0
    evictCounterBank2 = 0
    evictCounterBank3 = 0
    evictCounterBank4 = 0
    evictCounterBank5 = 0
    evictCounterBank6 = 0
    evictCounterBank7 = 0
    for line in ftrace:
        if int(line.split()[2]) < bank_partition:
            if int(line.split()[1]) == 0: 
                readCounterBank0 += 1
            elif int(line.split()[1]) == 1:
		writeCounterBank0 += 1
            elif int(line.split()[1]) == 3:
		evictCounterBank0 += 1
	elif int(line.split()[2]) < 2*bank_partition:
            if int(line.split()[1]) == 0: 
                readCounterBank1 += 1
            elif int(line.split()[1]) == 1:
		writeCounterBank1 += 1
            elif int(line.split()[1]) == 3:
		evictCounterBank1 += 1
	elif int(line.split()[2]) < 3*bank_partition:
            if int(line.split()[1]) == 0: 
                readCounterBank2 += 1
            elif int(line.split()[1]) == 1:
		writeCounterBank2 += 1
            elif int(line.split()[1]) == 3:
		evictCounterBank2 += 1
	elif int(line.split()[2]) < 4*bank_partition:
            if int(line.split()[1]) == 0: 
                readCounterBank3 += 1
            elif int(line.split()[1]) == 1:
		writeCounterBank3 += 1
            elif int(line.split()[1]) == 3:
		evictCounterBank3 += 1
	elif int(line.split()[2]) < 5*bank_partition:
            if int(line.split()[1]) == 0: 
                readCounterBank4 += 1
            elif int(line.split()[1]) == 1:
		writeCounterBank4 += 1
            elif int(line.split()[1]) == 3:
		evictCounterBank4 += 1
	elif int(line.split()[2]) < 6*bank_partition:
            if int(line.split()[1]) == 0: 
                readCounterBank5 += 1
            elif int(line.split()[1]) == 1:
		writeCounterBank5 += 1
            elif int(line.split()[1]) == 3:
		evictCounterBank5 += 1
	elif int(line.split()[2]) < 7*bank_partition:
            if int(line.split()[1]) == 0: 
                readCounterBank6 += 1
            elif int(line.split()[1]) == 1:
		writeCounterBank6 += 1
            elif int(line.split()[1]) == 3:
		evictCounterBank6 += 1
	elif int(line.split()[1]) == 0:
	    readCounterBank7 += 1
        elif int(line.split()[1]) == 1:
            writeCounterBank1 += 1
        elif int(line.split()[1]) == 3:
	    evictCounterBank1 += 1
fout = open('bank_access',"w") 
print >>fout, "Bank0:%-9s Bank1:%-9s Bank2:%-9s Bank3:%-9s Bank4:%-9s Bank5:%-9s Bank6:%-9s Bank7:%-9s" % (readCounterBank0, readCounterBank1, readCounterBank2, readCounterBank3, readCounterBank4, readCounterBank5, readCounterBank6, readCounterBank7)
print >>fout, "wBank0:%-9s wBank1:%-9s wBank2:%-9s wBank3:%-9s wBank4:%-9s wBank5:%-9s wBank6:%-9s wBank7:%-9s" % (writeCounterBank0, writeCounterBank1, writeCounterBank2, writeCounterBank3, writeCounterBank4, writeCounterBank5, writeCounterBank6, writeCounterBank7)
print >>fout, "eBank0:%-9s eBank1:%-9s eBank2:%-9s eBank3:%-9s eBank4:%-9s eBank5:%-9s eBank6:%-9s eBank7:%-9s" % (evictCounterBank0, evictCounterBank1, evictCounterBank2, evictCounterBank3, evictCounterBank4, evictCounterBank5, evictCounterBank6, evictCounterBank7)
fout.close()
