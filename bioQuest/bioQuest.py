from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio import motifs

nucleotideFasta = SeqIO.parse("genome.fasta", "fasta")
nucleotides = nucleotideFasta.next().seq

proteinsFasta = SeqIO.parse("MtrA_related_proteins.fasta", "fasta")
proteins = []
for protein_record in proteinsFasta:
    proteins.append(protein_record)

instances = [
	Seq("CACGAGG"),
	Seq("CACGCCG"),
	Seq("CACCCCG"),
	Seq("CACGGCG"),
]
motif = motifs.create(instances)

mass = [
	"CACGAGG",
	"CACGCCG",
	"CACCCCG",
	"CACGGCG",
]

def findSome(strInput):
	translatedNucleotides = strInput.translate(table=11)
	proteinsInNucleotides = []
	positions = []

	for prot in proteins:
	    pos = translatedNucleotides.find(prot.seq)
	    if(pos != -1):
	    	name = prot.name.split('|')[4]
	        proteinsInNucleotides.append(strInput[pos * 3 : pos * 3 + len(prot) * 3])
	        positions.append(str(name) + ':' + str(pos * 3 + 1))

	for pos in positions:
		number = int(pos.split(":")[1])
		substring = strInput[number - 300: number]
		motifsR = []
		counter = 0

		for position, seq in motif.instances.search(substring):
			arr = [position, pos.split(":")[0]]

			if(len(arr) != 0):
				print mass[counter], arr[1]

			counter += 1


findSome(nucleotides)
#findSome(nucleotides[1:])
#findSome(nucleotides[2:])

#nucleotides = Seq.reverse_complement(nucleotides)

#findSome(nucleotides)
#findSome(nucleotides[1:])
#findSome(nucleotides[2:])