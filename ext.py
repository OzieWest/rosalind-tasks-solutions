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
rna_dic = {}
rna_source = read_file('rna-codon-table.txt')
for val in rna_source:
	val = val.replace('\n', '')
	data = val.split(' ')
	rna_dic[data[0]] = data[1]

def rna_value_by_key(value):
	return rna_dic[value]


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