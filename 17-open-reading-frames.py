import math
import ext

n = 3
finalResult = {}

fasta = ext.Fasta().fromFile('rosalind_orf.txt');
key = fasta.getKeys()[0]
source = fasta.data[key]
source = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'

revSource = ext.rev_and_conv(source)

def find_orf(resDic, source):
	for i in range(0, len(source)):
		data = ext.splitBy(source[i:], n)
		if(len(data) > 1):
			flagStart = False
			flagStop = False
			sequence = ''
			for elm in data:
				if(ext.isStartCodon(elm) and flagStart == False):
					flagStart = True

				flagStop = ext.isStopCodon(elm)
				if(flagStop):
					break

				if(flagStart and len(elm) == 3):
					sequence += ext.dna_codon_table[elm]

			if(len(sequence) > 0):	
				resDic[sequence] = 1

find_orf(finalResult, source)
find_orf(finalResult, revSource)

for i in finalResult:
 	print i