__author__ = 'Navid Khoshavi'
import sys
import re


# access type = 0 = read
# access type = 1 = write
# access type = 2 = update
# access type = 3 = evict
# access type = 4 = prefetch
# access type = 5 = insert (MEM writes LLC) when LLC has a read miss
# access type = 6 = writeback (LLC writes MEM)


with open('llc_access_trace_sorted_short.log', 'rb') as fh:
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
#preSimCycleAccess: first write before the consequence read operations
fout = open("DSI.log","w")
with open('llc_access_trace_sorted.log', 'r') as ftrace:
    for line in ftrace:
        R_counter = 0
        W_counter = 0
        sim_cycle_dif = 0
        write2LastRead = 0
        DSI = 0
        largestDSI = 0
        avgWrite2LastRead = 0
        avgCoefficient = 0
        CL = int(line.split()[2])                # CL: Cache line
        preMemAccess = int(line.split()[1])      #preMemAccess: first memory access to cache line
        preSimCycleAccess = int(line.split()[0]) #preSimCycleAccess: first time access to cache line
        while CL == int(line.split()[2]):
            if (preMemAccess == 1 or preMemAccess == 2 or preMemAccess == 3 or preMemAccess == 4) and int(line.split()[1]) == 0: # compute how many times the memory access is changed to read access
                avgCoefficient += 1
            if int(line.split()[1]) == 0:
                sim_cycle_dif = int(line.split()[0]) - preSimCycleAccess
                DSI = sim_cycle_dif
                if largestDSI < DSI:
                    largestDSI = DSI
                R_counter += 1
                preMemAccess = int(line.split()[1])
                if int(line.split()[0]) == last_line:
                    break
                line = ftrace.next()
                i += 1
            elif int(line.split()[1]) == 1 or int(line.split()[1]) == 2 or int(line.split()[1]) == 3 or int(line.split()[1]) == 4:
                write2LastRead = (write2LastRead + sim_cycle_dif)
                sim_cycle_dif = 0
                W_counter += 1
                preSimCycleAccess = int(line.split()[0])
                preMemAccess = int(line.split()[1])
                if int(line.split()[0]) == last_line:
                    break
                line = ftrace.next()
                i += 1
            else:
                #preSimCycleAccess = int(line.split()[0])
                preMemAccess = int(line.split()[1])
                if int(line.split()[0]) == last_line:
                    break
                line = ftrace.next()
                i += 1
        # compute the average read access period
        if (avgCoefficient != 0):
            write2LastRead = (write2LastRead + sim_cycle_dif)
            avgWrite2LastRead = int(write2LastRead/avgCoefficient)

        print >>fout, "%-9s %-9s %-9s %-9d" % (CL, R_counter, W_counter, largestDSI)
        if int(line.split()[0]) != last_line:
            ftrace.seek(0)
            for y in xrange(0, i):
                line = ftrace.next()
        else:
            break
fout.close()


# fix me: in the second elsif, I have to consider the previous Mem access