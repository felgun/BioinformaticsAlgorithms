"""
	CountHammingDistance.py
"""

import argparse

def calculate_hamming_distance(s1, s2):
	"""
	Calculate the Hamming distance (number of mismatches) between two input strings.
	Returns the distance as an int. 
	Param:
		s1 {str}	: The first string to be compared. 
		s2 {str}	: The second string to be compared.
	"""
	distance = 0
	
	if len(s1) != len(s2):
		print("Error: Unable to calculate the Hamming distance because the lengths of "+
			"the two strings are different.")
	else:
		# Go through the two strings from the beginning to the end and count any mismatches found.
		for i in xrange(0,len(s1)):
			if s1[i] != s2[i]:
				distance += 1

	return distance


def parse_arg():
	"""
	Parses arguments.
	"""
	parser = argparse.ArgumentParser(description="Counting the Hamming distance between two strings of equal length.")
	parser.add_argument("--i",help="Path to the input file containing two lines of strings "+
						"having the same length. The Hamming distance between the two strings "+
						"will be calculated. ", type=str, required=True)

	return parser.parse_args()

def main():

	args = parse_arg()
	min_line = 2

	with open(args.i) as input_file:
		in_file_list = input_file.read().splitlines()

		if len(in_file_list) < min_line:
			print("Error: The input file shall contain two lines of strings having "+
				"the same length to be compared to each other. ")
		else:
			print(calculate_hamming_distance(in_file_list[0],in_file_list[1]))


if __name__ == '__main__':
	main()