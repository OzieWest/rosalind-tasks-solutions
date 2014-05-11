def read_file(file_name):
	with open(file_name) as f:
	    return f.readlines()

rna_dic = {}
rna_source = read_file('rna-codon-table.txt')
for val in rna_source:
	val = val.replace('\n', '')
	data = val.split(' ')
	rna_dic[data[0]] = data[1]

def rna_value_by_key(value):
	return rna_dic[value]