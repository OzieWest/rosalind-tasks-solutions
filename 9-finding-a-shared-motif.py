import math
import ext

source = ext.read_file('rosalind_lcsm.txt')

data = []
current = []
for ind, val in enumerate(source):
	val = val.replace('\n', '')
	if (val.startswith('>')):
		if(len(current) > 0):
			data.append(current)
		current = []
		current.append(val)
	else:
		if(len(current) > 1):
			current[1] += val
		else:
			current.append(val)
		if(len(source) - 1 == ind):
			data.append(current)

def check(data, val):
	result = False
	for elm in data:
		if (val in elm[1]):
			result = True
		else:
			result = False
	return result

count = 251
offset = 0
step = 1

counter = 0
elm = data[0][1]
for ind in range(0, len(data[0][1])):
	val = elm[ind: count + ind]
	if(check(data, val)):
		print len(val), val
		break

