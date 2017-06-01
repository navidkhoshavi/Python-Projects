__author__ = 'Navid Khoshavi'
#import sys
#import re
#from inspect import currentframe


def convToParent3x(a):
	b = ""
	if len(a) > 8:
		for i in range(0,5):
			b += str(a[i])
		for j in range(6,11):
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



def comp6Char(a,b):
	count = 0
	for i in range(0,5):
		if a[i] == b[i]:
			count += 1
	if count == 5:
		return True
	else:
		return False




with open('/media/nvidia/MyFile2/backup/TACO/dedup/addr/sensivity/sensivity_4.out', 'rb') as fh:
    first = next(fh)
    offs = -1
    while True:
        fh.seek(offs, 2)
        lines = fh.readlines()
        if len(lines)>1:
            last = lines[-1]
            break
        offs *= 2
    #print first
    #print last
    last_line = last.split()[0]



counter = 1
totalCount = 0
#prevLine = ""
nextLine = "0x00000"
newLine = ""
parent3x = ""
i = 0
flag = 0
my_list = [200]
fout = open('/media/nvidia/MyFile2/backup/TACO/dedup/addr/sensivity/sensivity_Z2_PhyAddr.out',"w")
ftrace = open('/media/nvidia/MyFile2/backup/TACO/dedup/addr/sensivity/sensivity_4.out', 'rb')
for line in ftrace:
	newLine = line.split()[0]
	parent3x = convToParent3x(newLine)
	while convToParent3x(newLine) == convToParent3x(nextLine) and line.split()[0]<= last_line:
		if line.split()[0] not in my_list:
			flag = 1
			if comp6Char(newLine,nextLine):
				counter += 1
				my_list.append(nextLine)
			if line.split()[0] != last_line:
				line = ftrace.next()
				nextLine = line.split()[0]
			elif line.split()[0] == last_line:
				nextLine = "0x00000"
				break
		elif line.split()[0] in my_list:
			break
	if counter != 1 or flag == 1:
		fout.write("%s %d \n" %(parent3x, counter))
		flag = 0
	nextLine = line.split()[0]
	ftrace.seek(0)
	i += counter - 1
	for y in xrange(0, i):
		line = ftrace.next()
	counter = 1
fout.close()
ftrace.close()



