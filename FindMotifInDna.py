"""
	FindMotifInDna.py
"""

import argparse
import os.path

def find_indexes_of_motif(dna_seq,pattern):
	"""
	Finds the indexes of motif/pattern (if found) in the DNA sequence. The indexes are 1-base.
	Returns a list of strings of the indexes where the pattern is found (the starting position).
	Param:
		dna_seq {str}	: The DNA sequence from which the pattern to be searched.
		pattern {str}	: The pattern/motif to be searched for.
	"""
	indexes = []

	if len(pattern) > len(dna_seq):
		print("Error: The pattern has a length of {0} while the DNA sequence has a length of {1}." +
				" The pattern to be searched has to be shorter or has equal length with "+
				"the DNA sequence.".format(len(pattern),len(dna_seq)))
		return indexes
	else:
		for i in xrange(0,len(dna_seq)-len(pattern)):
			if dna_seq[i:i+len(pattern)] == pattern:
				indexes.append(str(i+1))

	return indexes


def parse_arg():
	"""
	Parses arguments.
	"""
	parser = argparse.ArgumentParser(description="Find a motif in a DNA sequence.")
	parser.add_argument("--dna",help="The DNA sequence from which the pattern to be searched.",
							type=str,required=True)
	parser.add_argument("--pattern",help="The pattern to be searched for.",
							type=str,required=True)
	return parser.parse_args()

def main():
	args = parse_arg()
	print(" ".join(find_indexes_of_motif(args.dna,args.pattern)))

if __name__ == '__main__':
	main()