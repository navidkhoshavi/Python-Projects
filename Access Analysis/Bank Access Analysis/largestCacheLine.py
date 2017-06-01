__author__ = 'Navid Khoshavi'import sys

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
def largestCacheLine ():
    # find the largest CL number
    with open('llc_access_trace_sorted.log', 'r') as ftrace:
        largest = 0
    	for line in ftrace:
	    if (int(line.split()[2]) > largest):
                secondLargestCacheLine = largest
                largest = int(line.split()[2])              
    fout = open('output',"w") 
    print >>fout, "The Largest Cache Line number is:", largest
    print >>fout, "The second largest Cache Line number is:", secondLargestCacheLine
    fout.close()		
    return largest;


largestCacheLine ();



