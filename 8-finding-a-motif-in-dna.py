import ext
import math

source = ext.read_file('rosalind_subs.txt')

data = []
for elm in source:
	data.append(elm.replace('\n', ''))

result = []
for elm in ext.all_indices(data[0], data[1]):
	result.append(elm + 1)

print result