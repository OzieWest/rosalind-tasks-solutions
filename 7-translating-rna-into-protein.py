import math
import ext

data_source = ext.read_file('rosalind_prot.txt')[0]

n = 3
arr = [data_source[i:i+n] for i in range(0, len(data_source), n)]

result = ''
for val in arr:
	step = ext.rna_value_by_key(val)
	if(step == 'Stop'):
		break
	result += step

print result