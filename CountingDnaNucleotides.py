"""
CountingDnaNucleotides.py

"""
import argparse
import os.path

def count_dna_nucleotides(sequence):
    counts = {'A':0,'C':0,'G':0,'T':0}
    for i in xrange(0,len(sequence)):
        if sequence[i] in counts:
            counts[sequence[i]] += 1
        else:
            print("Warning: {0} is not part of valid DNA nucleotides: {1}".format(
                    sequence[i],counts.keys()))
    print("{0} {1} {2} {3}".format(counts['A'],counts['C'],counts['G'],counts['T'],))
    return counts

def parse_arg():
    parser = argparse.ArgumentParser(description="Counting dna nucleotide in a sequence")
    parser.add_argument("--seq",help="DNA sequence of which nucleotides to be counted", type=str, required=False)
    parser.add_argument("--file",help="Path to the input file containing DNA sequence(s) of which nucleotides to be counted", type=str, required=False)
    return parser.parse_args()

def main():
    args = parse_arg()
    # Check if the input sequence is specified using at least --seq or --file
    if args.seq is None and args.file is None:
    	print("Error: Please specify the input sequence using at least --seq or --file. ")
    else:
	    # Count the nucleotides from the sequence specified through --seq 
	    if args.seq :
	    	count_dna_nucleotides(args.seq)
	    	print
	    # Count the nucleotides from the sequence specified through --file, line by line
	    if args.file:
	    	# Check if the path specified is a file 
	    	if os.path.isfile(args.file):	
	    		with open(args.file) as input_file:
	    			sequences = input_file.read().splitlines()
		    	for line in sequences:
		    		print(str(line))
		    		count_dna_nucleotides(line)
		    		print
    		else:
    			print("Error: The path specified in --file is not a file.")


if __name__ == '__main__':
    main()