"""
	TranscribeDnaToRna.py
"""
import argparse
import os.path

def transcribe_dna(dna_seq):
	"""
	Transcribes the DNA sequence into RNA sequence by replacing 'T' with 'U' and prints the result.
	Returns a string of RNA sequence from the transcribed DNA. 
	Param:
		dna_seq {str} : The DNA sequence to be transcribed.
	"""
	rna_seq = dna_seq.replace('T','U')
	print(rna_seq)
	return rna_seq

def parse_arg():
	"""
	Parses the arguments.
	"""
	parser = argparse.ArgumentParser(description="Transcribing DNA into RNA by replacing 'T' with 'U'")
	parser.add_argument("--seq",help="DNA sequence to be transcribed into RNA",required=False)
	parser.add_argument("--file",help="Path to the input file containing the" +

							" DNA sequence(s) to be transcribed into RNA",required=False)
	return parser.parse_args()

def main():
	args = parse_arg()

	# Check if the input sequence is specified using at least --seq or --file
	if args.seq is None and args.file is None:
		print("Error: Please specify the input sequence using at least --seq or --file. ")
	else:
		# Transcribe the sequence specified through --seq
		if args.seq:
			transcribe_dna(args.seq)
			print
	    # Transcribe the sequence(s) specified through --file, line by line
		if args.file:
	    	# Check if the path specified is a file 
			if os.path.isfile(args.file):
				with open(args.file) as input_file:
					dna_sequences = input_file.read().splitlines()
				for i in xrange(0,len(dna_sequences)):
					# Print the line number, then the transcribed sequence 
					print("line {0}:".format(i+1))
					transcribe_dna(dna_sequences[i])
					print
			else:
				print("Error: The path specified in --file is not a file.")

if __name__ == '__main__':
	main()