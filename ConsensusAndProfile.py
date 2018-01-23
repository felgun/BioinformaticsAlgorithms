"""
	ConsensusAndProfile.py
"""
import argparse
import os.path

def get_sequences_from_fasta(in_file_list):
	"""
	Returns a list containing only the sequences from a list generated form file with FASTA format. 
	The sequences per read will be stored as one element in the list.
	Param:
		in_file_list {list} : A list from reading a file. The file is expected to be in FASTA format.
	"""
	seq = [] # List for storing all the reads sequences. 
	sequence = [] # List for storing the sequences for one read.
	description_indicator = ">"
	prev_line_is_description = False

	for line in in_file_list:
		if line.startswith(description_indicator):
			if prev_line_is_description:
				print("Warning: A description line is found right after another description (no sequence).")
			prev_line_is_description = True
			if len(sequence) > 0:
				seq.append("".join(sequence))
			sequence = []
		else:
			prev_line_is_description = False
			sequence.append(line.rstrip())

	if len(sequence) > 0:
		seq.append("".join(sequence))

	return seq

def get_consensus_from_profile(profile,bases):
	"""
	Returns the consensus sequence based on the profile matrix provided. The evaluation order is based on the 
	order of the base in bases list. If the highest/max count for a position in the profile matrix are found in 
	multiple bases, the base with earlier order in bases list will be chosen. 
	Param:
		profile {2D array} 	: A profile matrix of sequences. The height represents the base (base index), 
								The width represent the (0-based) position in the sequence.
		bases {list}		: A list of valid bases that are counted for the profile matrix. 
	"""
	consensus_list = []
	all_empty = "-"

	if len(profile) != len(bases):
		print("Error: The profile matrix has a length of {}, while there is {} given bases {}. ".format(
				len(profile), len(bases), bases))
	else:
		for j in xrange(0,len(profile[0])):
			max_count = 0
			max_count_base = all_empty
			for i in xrange(0,len(profile)):
				if profile[i][j] > max_count:
					max_count = profile[i][j]
					max_count_base = bases[i]
			consensus_list.append(max_count_base)

	return "".join(consensus_list)

def get_consensus_and_profile(in_file_list):
	"""
	Gets the sequence consensus and the profile matrix from the list generated from reading the input file. 
	Returns a three-element-tuple (consensus, profile, bases) where: 
		- consensus is a string of the consensus sequence. For details, see get_consensus_from_profile function.
		- profile is a 2D array containing the profile matrix of the sequences found in the input file.
		- bases is a list of valid bases that are used for counting/creating the profile matrix. 
	Param:
		in_file_list {list} : A list from reading a file. The file is expected to be in FASTA format.
	"""
	consensus = ""
	bases = ["A","C","G","T"]

	input_sequences = get_sequences_from_fasta(in_file_list)
	if len(input_sequences) > 0:
		length_of_seq = len(input_sequences[0])
		profile = [[0 for n in xrange(length_of_seq)] for m in xrange(len(bases))]
		for i in xrange(0,len(input_sequences)):
			x = length_of_seq
			if len(input_sequences[i]) < length_of_seq:
				print("Warning: The {}-th sequence in the file has a shorter length than the first sequence in the file ({}). "
						+"However, the length of the first sequence will be used for the profile matrix.".format(i+1,length_of_seq))
				x = len(input_sequences[i])
			if len(input_sequences[i]) < length_of_seq:
				print("Warning: The {}-th sequence in the file has a longer length than the first sequence in the file ({}). "
						+"However, the length of the first sequence will be used for the profile matrix. "
						+"Any bases after {}-th position will be ignored".format(i+1,length_of_seq,length_of_seq))
			for j in xrange(0,x):
				if input_sequences[i][j] in bases:
					base_index = bases.index(input_sequences[i][j])
					profile[base_index][j] += 1
		consensus = get_consensus_from_profile(profile,bases)
	else:
		print("Warning: No sequences exist in the provided file.")
		profile = [[0] for m in xrange(len(bases))]

	return (consensus,profile,bases)

def parse_arg():
	"""
	Parses the arguments. 
	"""
	parser = argparse.ArgumentParser(
					description="Finds a consensus string and profile matrix for the collection of DNA sequences.")
	parser.add_argument("--file",help="A file with FASTA format, containing the sequences to be profiled.",
						type=str,required=True)
	return parser.parse_args()


def main():
	args = parse_arg()

	if os.path.isfile(args.file):
		with open(args.file) as input_file:
			in_file_list = input_file.read().splitlines()
			(consensus,profile,bases) = get_consensus_and_profile(in_file_list)
			print(consensus)
			for i in xrange(0,len(bases)):
				print("{}: {}".format(bases[i]," ".join(str(x) for x in profile[i])))

	else:
		print("Error: The argument specified for --file is not a valid path to a file.")	

if __name__ == '__main__':
	main()