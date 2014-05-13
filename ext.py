def read_file(file_name):
	with open(file_name) as f:
	    return f.readlines()

#---------------------------------------------------------
rna_dic = {}
rna_source = read_file('rna-codon-table.txt')
for val in rna_source:
	val = val.replace('\n', '')
	data = val.split(' ')
	rna_dic[data[0]] = data[1]

def rna_value_by_key(value):
	return rna_dic[value]

#---------------------------------------------------------
mono_mass_table = {}
mono_mass_source = read_file('monoisotopic-mass-table.txt')
for val in mono_mass_source:
	val = val.replace('\n', '')
	data = val.split('   ')
	mono_mass_table[data[0]] = data[1]

def get_monomass(value):
	return mono_mass_table[value]

#---------------------------------------------------------
def all_indices(string, sub, listindex=[], offset=0):
    i = string.find(sub, offset)
    while i >= 0:
        listindex.append(i)
        i = string.find(sub, i + 1)
    return listindex