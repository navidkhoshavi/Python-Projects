__author__ = 'Navid Khoshavi'
#!/usr/bin/python -O

# This file compute the average access to cachelines in L2
# Make sure you have fed this program with your L2 tracefile


import sys
import re

# access type = 0 = read
# access type = 1 = write
# access type = 2 = update
# access type = 3 = evict
# access type = 4 = prefetch
# access type = 5 = insert (MEM writes LLC) when LLC has a read miss
# access type = 6 = writeback (LLC writes MEM)


# pre-state = X, current-state = 0(read) ==> the cache line needs to be refreshed
# pre-state = X, current-state = 1(write) ==> no refresh required
# pre-state = X, current-state = 2(update) ==> no refresh required
# pre-state = X, current-state = 3(evict) ==> don't care

# Considered inter access period
# 100 simulation cycle
# 1K simulation cycle
# 10K simulation cycle
# 100K simulation cycle
# 1M simulation cycle
# 10M simulation cycle
# more than 10M simulation cycle

with open('LLC1.dat', 'rb') as fh:
    first = next(fh)
    offs = -100
    while True:
        fh.seek(offs, 2)
        lines = fh.readlines()
        if len(lines)>1:
            last = lines[-1]
            break
        offs *= 2
    last_line = int(last.split()[0])

i = 0
R_counter = 0
W_counter = 0
avg_sim_cycle = 0
num_0rows = 0
num_line = [0] * 246846
avgR_sim_cycle = [0] * 246846
avgW_sim_cycle = [0] * 246846


# Read inter-access
lineR1K = 0
lineR10K = 0
lineR100K = 0
lineR1M = 0
lineRMore1M = 0

# Write inter-access
lineW1K = 0
lineW10K = 0
lineW100K = 0
lineW1M = 0
lineWMore1M = 0

fout = open("LLC1_out.dat","w")
print >>fout, "Line num, avg_WR_sim_cycle"
fout.close()
with open('LLC1.dat', 'r') as ftrace:
    for line in ftrace:
        pre_state = -1
        row_exist = 0
        pre_row_sim = 0
        row = int(line.split()[2])
        pre_state = int(line.split()[1])
        pre_row_sim = int(line.split()[0])
        if row == 0:
            num_0rows += 1
        if num_line.count(row) == 1: #if the line has been already counted, change flag to 1 and avoid to count it again
            row_exist = 1
        if row == 0 and num_0rows > 1:
            ftrace.seek(0)
            i += 1
            for y in xrange(0, i):
                line = ftrace.next()
        #FIX me, wrong result by Tuesday 03/01/2015
        elif row_exist == 0 and int(line.split()[0]) <= last_line:
            while int(line.split()[0]) < last_line:
                if int(line.split()[2]) == row:
                    sim_cycle_dif = int(line.split()[0]) - pre_row_sim
                    if int(line.split()[1]) == 0:
                        if sim_cycle_dif <= 1000:
                            lineR1K += 1
                        elif sim_cycle_dif <= 10000:
                            lineR10K += 1
                        elif sim_cycle_dif <= 100000:
                            lineR100K += 1
                        elif sim_cycle_dif <= 1000000:
                            lineR1M += 1
                        elif sim_cycle_dif > 1000000:
                            lineRMore1M += 1
                        R_counter += 1
                        avgR_sim_cycle[i] = (avgR_sim_cycle[i] + sim_cycle_dif)/(R_counter)
                        pre_row_sim = int(line.split()[0])
                        line = ftrace.next()
                    elif int(line.split()[1]) == 1 or int(line.split()[1]) == 2:
                        if sim_cycle_dif <= 1000:
                            lineW1K += 1
                        elif sim_cycle_dif <= 10000:
                            lineW10K += 1
                        elif sim_cycle_dif <= 100000:
                            lineW100K += 1
                        elif sim_cycle_dif <= 1000000:
                            lineW1M += 1
                        elif sim_cycle_dif > 1000000:
                            lineWMore1M += 1
                        W_counter += 1
                        avgW_sim_cycle[i] = (avgW_sim_cycle[i] + sim_cycle_dif)/(W_counter)
                        pre_row_sim = int(line.split()[0])
                        line = ftrace.next()
                    else:
                        pre_row_sim = int(line.split()[0])
                        line = ftrace.next()
                        break
                else:
                    line = ftrace.next()
            num_line[i] = row
            R_counter = 0
            W_counter = 0
            ftrace.seek(0)
            i += 1
            for y in xrange(0, i):
                line = ftrace.next()
        elif row_exist != 0 and int(line.split()[0]) < last_line:
            i += 1
            ftrace.seek(0)
            for y in xrange(0, i):
                line = ftrace.next()
        else:
            fout = open("LLC1_out.dat","w")
            print >>fout, "lineR1K = %d, lineR10K = %d, lineR100K = %d, lineR1M = %d, lineRMore1M = %d, lineW1K = %d, lineW10K = %d, lineW100K = %d, lineW1M = %d, lineWMore1M = %d" %(lineR1K,lineR10K,lineR100K,lineR1M,lineRMore1M,lineW1K,lineW10K,lineW100K,lineW1M,lineWMore1M)
            fout.close()
            break



