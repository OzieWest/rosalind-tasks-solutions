import math
import ext

count = 0
source = ext.read_file('rosalind_hamm.txt')

for elm in source:
	elm = elm.replace('\n', '')

for i in range(0, len(source[0]) - 1):
	first_char = source[0][i]
	second_char = source[1][i]
	#print first_char, second_char

	if(first_char != second_char):
		count += 1

print count