import math
import ext

fasta = ext.Fasta().fromFile('rosalind_grph.txt')

counter = 0
for i in fasta.data:
	val = fasta.data[i]
	for j in fasta.data:
		if(i != j):
			b = fasta.data[j]
			if(b.startswith(val[-3:])):
				counter += 1
				print i, j

print counter, len(fasta.data)