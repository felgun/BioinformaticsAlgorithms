"""
	TranslateRnaToProtein.py
"""

import argparse
import os.path

def translate_rna_to_protein(rna_seq):
	"""
	Translates the rna sequence to a protein sequence.
	Returns the protein sequence as a string. 
	Param: 
		rna_seq	{str} 	: The RNA sequence to be translated. 
	"""

	# dictionary containing each codon (3 base sequences) translation
	codon_dict = {"UUU":"F","UUC":"F","UUA":"L","UUG":"L",
					"UCU":"S","UCC":"S","UCA":"S","UCG":"S",
					"UAU":"Y","UAC":"Y","UAA":"Stop","UAG":"Stop",
					"UGU":"C","UGC":"C","UGA":"Stop","UGG":"W",
					"CUU":"L","CUC":"L","CUA":"L","CUG":"L",
					"CCU":"P","CCC":"P","CCA":"P","CCG":"P",
					"CAU":"H","CAC":"H","CAA":"Q","CAG":"Q",
					"CGU":"R","CGC":"R","CGA":"R","CGG":"R",
					"AUU":"I","AUC":"I","AUA":"I","AUG":"M",
					"ACU":"T","ACC":"T","ACA":"T","ACG":"T",
					"AAU":"N","AAC":"N","AAA":"K","AAG":"K",
					"AGU":"S","AGC":"S","AGA":"R","AGG":"R",
					"GUU":"V","GUC":"V","GUA":"V","GUG":"V",
					"GCU":"A","GCC":"A","GCA":"A","GCG":"A",					
					"GAU":"D","GAC":"D","GAA":"E","GAG":"E",
					"GGU":"G","GGC":"G","GGA":"G","GGG":"G",
					}
	codon_length = 3
	stop_code = "Stop"
	unknown_code = "?"
	protein_seq = [] #Store the sequence in a list before converting it to a string to save memory.

	# Go through the RNA sequence from beginning to the end, 
	# but with index increment of the codon length
	for i in xrange(0,len(rna_seq),codon_length):
		# Check if the index + codon length will still within the length of RNA sequence.
		if (i+codon_length) <= len(rna_seq):
			codon = rna_seq[i:(i+codon_length)]
			# Check if the codon exists in the dictionary. 
			# If so, get the translation. 
			if codon in codon_dict:
				translation = codon_dict[codon]
				# If the translation is stop code, return the protein sequence. 
				if translation == stop_code:
					return "".join(protein_seq)
				# Otherwise, append the translation to the protein sequence. 
				else:
					protein_seq.append(translation)
			else:
				print("The sequence {0} is not valid. The translation will be coded as '?'").format(
					codon)

	print("Warning: no stop codon found. ")
	return "".join(protein_seq)

def parse_arg():
	"""
	Parses arguments.
	"""
	parser = argparse.ArgumentParser(description="Counting dna nucleotide in a sequence")
	parser.add_argument("--seq",help="RNA sequence to be tranlated into protein", type=str, required=False)
	parser.add_argument("--file",help="Path to the input file containing RNA sequence(s) to be tranlated into protein", type=str, required=False)
	return parser.parse_args()

def main():
	args = parse_arg()
	# Check if the input sequence is specified using at least --seq or --file
	if args.seq is None and args.file is None:
		print("Error: Please specify the input sequence using at least --seq or --file. ")
	else:
		# Count the nucleotides from the sequence specified through --seq 
		if args.seq :
			print(translate_rna_to_protein(args.seq))
			print
		# Count the nucleotides from the sequence specified through --file, line by line
		if args.file:
			# Check if the path specified is a file 
			if os.path.isfile(args.file):	
				with open(args.file) as input_file:
					sequences = input_file.read().splitlines()
					for line in sequences:
						print(str(line))
						print("Translates to:")
						print(translate_rna_to_protein(line))
						print
			else:
				print("Error: The path specified in --file is not a file.")


if __name__ == '__main__':
	main()