__author__ = 'Navid Khoshavi'
fout = open('blackscholes/PhyAddr/addr/sensivity/sensivity_4.out',"w") 
ftrace = open('blackscholes/PhyAddr/addr/bk.BankTLB.out.sorted', 'rb')
counter = 1
prevLine = ""
newLine = ""
flag = 0
for line in ftrace:
	newLine = line.split()[0]
	if newLine == prevLine:
		counter += 1
		if counter > 4:
		    flag = 1
	elif newLine != prevLine:
		if flag == 1:
		    fout.write("%s\n" %prevLine)
		    counter = 1
		    flag = 0
		counter = 1
	prevLine = newLine
fout.close()
ftrace.close()


