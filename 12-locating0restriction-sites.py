import math
import ext

fasta = ext.FastaF('rosalind_revp.txt')
value = [fasta.data[i] for i in fasta.data][0]

a = 'TCAATGCATGCGGGTCTATATGCAT'
b = a[::-1]

pos = 5
l = pos + 4

print a
print b
