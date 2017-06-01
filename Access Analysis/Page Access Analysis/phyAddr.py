__author__ = 'Navid Khoshavi'
#import sys
#import re
#from inspect import currentframe


def convToPhy(a):
	b = ""
	if len(a) > 8:
		for i in range(0,4):
			b += str(a[i])
		for j in range(5,11):
			b += '0'
		return b
	elif len(a) > 6: 
		for i in range(0,4):
			b += str(a[i])
		for j in range(5,9):
			b += '0'
		return b
	elif len(a) > 4: 
		for i in range(0,4):
			b += str(a[i])
		b += '00'
		return b

def convToParentAddr(a):
	b = ""
	if len(a) > 8:
		for i in range(0,6):
			b += str(a[i])
		for j in range(7,11):
			b += 'x'
		return b
	elif len(a) > 6:
		for i in range(0,6):
			b += str(a[i])
		b += 'xx'
		return b
	elif len(a) > 4: 
		for i in range(0,5):
			b += str(a[i])
		b += 'x'
		return b

def convToParent3x(a):
	b = ""
	if len(a) > 8:
		for i in range(0,6):
			b += str(a[i])
		for j in range(7,11):
			b += 'x'
		return b
	elif len(a) > 6:
		for i in range(0,5):
			b += str(a[i])
		b += 'xxx'
		return b
	elif len(a) > 4:
		for i in range(0,5):
			b += str(a[i])
		b += 'xx'
		return b

def comp7Char(a,b):
	count = 0
	if len(a) > 8:
	    for i in range(0,6):
		    if a[i] == b[i]:
			    count += 1
	    if count == 6:
		    return True
	    else:
		    return False
	elif len(a) > 6:
	    for i in range(0,6):
		    if a[i] == b[i]:
			    count += 1
	    if count == 6:
		    return True
	    else:
		    return False

def comp6Char(a,b):
	count = 0
	for i in range(0,5):
		if a[i] == b[i]:
			count += 1
	if count == 5:
		return True
	else:
		return False

def comp5Char(a,b):
	count = 0
	for i in range(0,4):
		if a[i] == b[i]:
			count += 1
	if count == 4:
		return True
	else:
		return False




fout = open('swaptions/PhyAddr/addr/Phy_extr.out',"w") 
ftrace = open('swaptions/PhyAddr/addr/swaptions.BankTLB.out.sorted', 'rb')
counter = 1
totalCount = 0
firstTimeFlag = True
prevLine = ""
newLine = ""
PhyLine = ""
PhyPrevLine = ""
parentAddr = ""
parentPrevAddr = ""
counter3x = 0
for line in ftrace:
	newLine = line.split()[0]
	PhyLine = convToPhy(newLine)  # write first 5 chars+ five 0's
	PhyPrevLine = convToPhy(prevLine)
	parentAddr = convToParentAddr(newLine)  # write first 7 chars+ three x's
	parentPrevAddr = convToParentAddr(prevLine)  # write first 7 chars+ three x's
	parent3x = convToParent3x(prevLine)  # write first 7 chars+ three x's
	if firstTimeFlag == False:
		if comp7Char(newLine,prevLine):
			#fout.write("		%s\n" %newLine)
			counter += 1
		elif comp5Char(newLine,prevLine):
			if comp6Char(newLine,prevLine):
			    counter3x += counter
			    totalCount += counter
			    fout.write("	%s: parent2X (%d accesses)\n" %(parentPrevAddr,counter))
			    #fout.write("		%s\n" %newLine)
			    counter = 1
 			else:
			    counter3x += counter
			    fout.write("	%s: parent2X (%d accesses)\n" %(parentPrevAddr,counter))
			    fout.write("	>>>%s: Total parent3x(%d accesses)<<<\n" %(parent3x,counter3x))
			    #fout.write("		%s\n" %newLine)
			    totalCount += counter
			    counter = 1
			    counter3x = 0
		else:
			fout.write("	%s: Total Access(%d accesses)\n" %(parentPrevAddr,counter))
			counter3x += counter
			fout.write("	>>>%s: Total parent3x(%d accesses)<<<\n" %(parent3x,counter3x))
			totalCount += counter
			fout.write("Paddr %s:Total Accesses to this page file(%d accesses)\n" %(PhyPrevLine,totalCount))
			fout.write("==============\n")
			totalCount = 0
			counter3x = 0
			fout.write("Paddr %s:\n" %PhyLine)
			#fout.write("		%s\n" %newLine)
			counter = 1
	elif firstTimeFlag == True:
		firstTimeFlag = False
		fout.write("Paddr %s:\n" %PhyLine)
		#fout.write("		%s\n" %newLine)
		#print >> fout, '		%s' %(newLine)
	prevLine = newLine

fout.close()
ftrace.close()


