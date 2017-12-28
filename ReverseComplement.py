"""
ReverseComplement.py

"""
import argparse
import os.path

def reverse_complement(sequence):
	"""
	Creates, prints out, and returns the reverse complement of the input DNA sequence. 
	If the sequence contains any bases other than A, C, G, and T, the complement 
		of the base/character will be written as 'N'.
	Returns the reverse complement of the input DNA sequence as a string.
	Param:
		sequence {str} : The DNA sequence to be reverse complemented.
	"""
	base_complement = {'A':'T',
						'C':'G',
						'G':'C',
						'T':'A'}
	unknown = 'N'
	rev_comp_list = []
	rev_comp_string = ""

	# If the file does not contain anything, return an empty string
	if len(sequence) < 1:
		return rev_comp_string

	for i in xrange(0,len(sequence)):
		# Check the complement of each base in reverse order 
		#	(from last in the sequence to the beginning)
		base = sequence[len(sequence)-i-1]
		# If the base is either A, C, G, or T, then append the complement to the list
		if base in base_complement:
			rev_comp_list.append(base_complement[base])
		# Other than that, append unknown ("N") instead
		else:
			rev_comp_list.append(unknown)

	rev_comp_string = "".join(rev_comp_list)
	print rev_comp_string
	return rev_comp_string


def parse_arg():
	"""
	Parses the arguments. 
	"""
	parser = argparse.ArgumentParser(description="Reverse complement the "+
		"input DNA sequence.")
	parser.add_argument("--seq",help="The DNA sequence to be reverse complemented.",type=str,required=False)
	parser.add_argument("--file",help="A path to the file containing "+
							"the DNA sequence(s) to be reverse complemented.",type=str,required=False)
	return parser.parse_args()

def main():
	args = parse_arg()
	# Check if the input sequence is specified using at least --seq or --file
	if args.seq is None and args.file is None:
		print("Error: Please specify the input sequence using at least --seq or --file. ")
	else:
    	# Create the reverse complement of the sequence specified through --seq 
	    if args.seq :
	    	reverse_complement(args.seq)
	    	print
	    # Create the reverse complement of the sequence specified through --file, line by line
	    if args.file:
	    	# Check if the path specified is a file 
	    	if os.path.isfile(args.file):
	    		with open(args.file) as input_file:
	    			sequences = input_file.read().splitlines()
	    		for i in xrange(0, len(sequences)):
	    			print("line {0}: ".format(i+1))
	    			reverse_complement(sequences[i])
	    			print
	    	else:
	    		print("Error: The path specified in --file is not a file.")



if __name__ == '__main__':
	main()