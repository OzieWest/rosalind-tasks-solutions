import urllib2

def readFile(file_name):
	with open(file_name) as f:
		return f.read().splitlines()

class Fasta:
	info = ''
	data = {}

	# get Proteins from file
	def fromFile(self, file_name):
		sourceData = readFile(file_name)
		self.mapData(sourceData)
		return self

	# download Protein from web
	def fromWeb(self, name):
		response = urllib2.urlopen('http://www.uniprot.org/uniprot/' + name + '.fasta')
		sourceData =  response.read().splitlines()
		for ind, row in enumerate(sourceData):
			if(row.startswith('>')):
				self.info = row
				sourceData[ind] = name
				break
		self.mapData(sourceData)
		return self

	# convert one format to another
	def mapData(self, sourceData):
		current = []
		for ind, val in enumerate(sourceData):
			if (val.startswith('>')):
				if(len(current) > 0):
					self.data[current[0]] = current[1]
				current = []
				current.append(val[1:])				
			else:
				if(len(current) > 1):
					current[1] += val
				else:
					current.append(val)

				if(len(sourceData) - 1 == ind):
					self.data[current[0]] = current[1]

	# return value by key
	def getByKey(self, key):
		return self.data[key]

	# return all keys
	def getKeys(self):
		return [i for i in self.data]


# ========================================================================
def read_file(file_name):
	with open(file_name) as f:
	    return f.readlines()


# ========================================================================
rna_codon_table = {}
rna_source = read_file('rna-codon-table.txt')
for val in rna_source:
	val = val.replace('\n', '')
	data = val.split(' ')
	rna_codon_table[data[0]] = data[1]

def rna_value_by_key(value):
	return rna_codon_table[value]

dna_codon_table = {
	'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
	'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
	'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
	'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
	'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
	'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
	'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
	'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
	'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
	'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
	'TAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
	'TAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
	'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
	'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
	'TGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
	'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}

# ========================================================================
mono_mass_table = {}
mono_mass_source = read_file('monoisotopic-mass-table.txt')
for val in mono_mass_source:
	val = val.replace('\n', '')
	data = val.split('   ')
	mono_mass_table[data[0]] = data[1]

def get_monomass(value):
	return mono_mass_table[value]


# ========================================================================
def all_indices(string, sub, listindex=[], offset=0):
    i = string.find(sub, offset)
    while i >= 0:
        listindex.append(i)
        i = string.find(sub, i + 1)
    return listindex

def Fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fib(n-1)+Fib(n-2)

def splitBy(source, n):
	return [source[i:i+n] for i in range(0, len(source), n)]

def rev_and_conv(source):
	source = source[::-1]
	result = ''
	for char in source:
		if(char == 'T'):
			result += 'A'
		elif(char == 'A'):
			result += 'T'
		elif(char == 'C'):
			result += 'G'
		elif(char == 'G'):
			result += 'C'

	return result

def isStartCodon(elm):
	return elm == 'ATG' or elm == 'AUG'

def isStopCodon(elm):
	return elm == 'TAA' or elm == 'TGA' or elm == 'TAG' or elm == 'UAA' or elm == 'UGA' or elm == 'UAG'