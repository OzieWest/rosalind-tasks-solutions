import math
import ext

source = ext.read_file('rosalind_prtm.txt')[0]
source = source.replace('\n', '')

all_mass = 0.0

for char in source:
	val = ext.get_monomass(char)
	all_mass += float(val)

print all_mass
