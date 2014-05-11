import math

def percentage(part, whole):
  return 100 * float(part)/float(whole)

def perGC(val):
	return round(percentage(val.count('G') + val.count('C'), len(val)), 6)

sourceData = []
with open('rosalind_gc.txt') as f:
    sourceData = f.readlines()

dataArray = []
current = []
for ind, val in enumerate(sourceData):
	val = val.replace('\n', '')
	if (val.startswith('>')):
		if(len(current) > 0):
			dataArray.append(current)
		current = []
		current.append(val)
	else:
		if(len(current) > 1):
			current[1] += val
		else:
			current.append(val)
		if(len(sourceData) - 1 == ind):
			dataArray.append(current)

values = []
for d in dataArray:
	print d[0], perGC(d[1])
	values.append(perGC(d[1]))

print max(values)
