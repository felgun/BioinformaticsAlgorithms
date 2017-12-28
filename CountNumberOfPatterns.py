"""
	CountNumberOfPatterns.py
"""
import argparse
import os.path

def pattern_count(text,pattern):
	"""
	Counts the number of times pattern appears in text (including overlapping pattern).
	Return the number as an int.
	Param:
		text {str} 		: The text where the pattern to be searched for.
		pattern {str}	: The pattern to be searched for. 
	"""
	count = 0
	# Check for pattern by sliding a window in text with a size of the pattern's length
	for i in xrange(0,(len(text)-len(pattern))):
		if text[i:(i+len(pattern))] == pattern:
			count += 1
	return count

def parse_arg():
	"""
	Parses the arguments.
	"""
	parser = argparse.ArgumentParser("Counts the number of times a pattern appears in a text.")
	parser.add_argument("--file",help="Path to the input file. The input file shall " +
							"contains the text (where the pattern to be searched for) in the first line, "+
							"and contains the pattern to be searched in the second line",
							type=str,required=True)
	return parser.parse_args()

def main():
	args = parse_arg()
	with open(args.file) as input_file:
		in_file_list = input_file.read().splitlines()

		if len(in_file_list) >= 2:
			text = in_file_list[0].rstrip()
			pattern = in_file_list[1].rstrip()
			print(pattern_count(text,pattern))

if __name__ == '__main__':
	main()