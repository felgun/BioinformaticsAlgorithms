"""
	ComputeGCContent.py
"""

import argparse
import os.path

def count_gc_pct(sequence):
	"""
	Calculate the GC percent of the sequence. 
	Returns the GC percent of the sequence as a float.
	Param:
		sequence {str}	: The sequence of which GC percent is to be calculated.  
	"""
	gc_pct = float(0)
	gc_count = 0

	if len(sequence) == 0:
		return gc_pct

	# Check each character in the sequence. 
	# If it's either 'C' or 'G', then increment the GC count.
	for i in xrange(0,len(sequence)):
		if sequence[i] == 'C' or sequence[i] == 'G':
			gc_count += 1

	gc_pct = float(gc_count)/float(len(sequence)) * 100.000000
	print("GC count: {0}\tSeq len: {1}\tPct:{2}".format(gc_count,len(sequence),gc_pct))

	return gc_pct

def find_read_with_most_gc(list_data):
	"""
	Compute the GC content from each read from the input file data
		and find the read with the highest GC content.
	Returns a tuple (read name, GC percent) of the read with highest GC content.
	Param:
		list_data {list}	: The content of the input file after being read. 
	"""
	highest_gc_name = ""
	highest_gc_pct = float(0)
	prev_is_name = False
	name_indicator = '>'
	read_name = "" 
	seq_list = []

	# Go through the list of data from input file line by line.
	for i in xrange(0,len(list_data)):
		# Check if this line is the read name by checking the prefix, or if it's the 
		# last line in the file. 
		if list_data[i].startswith(name_indicator) or i == len(list_data) - 1:
			# If it's the last line in file, append the line to the sequence list.
			if i == len(list_data) - 1:
				seq_list.append(list_data[i].rstrip())
			# Check if the sequnce list has any value(s). 
			# If it does, calculate the GC content of the sequences 
			# and compare it to the highest value on the record. 
			if len(seq_list) > 0:
				seq = "".join(seq_list)
				gc_pct = count_gc_pct(seq)
				# Check if the GC content current read is higher than the current 
				# highest on the record. 
				# If so, replace the highest value and the name.
				if gc_pct > highest_gc_pct:
					highest_gc_pct = gc_pct
					highest_gc_name = read_name
				# If they are the same, append the name. 
				elif gc_pct == highest_gc_pct:
					highest_gc_name = highest_gc_name + ", " + read_name
				seq_list = []
			# If this line is the read name, update the read name record. 
			if list_data[i].startswith(name_indicator):
				prev_is_name = True
				read_name = list_data[i][1:]
		# If the line does not start with the name prefix, it should be the read sequence. 
		# Append the sequence (line) to the list.
		else:
			seq_list.append(list_data[i].rstrip())
				
	return (highest_gc_name,highest_gc_pct)

def parse_arg():
	parser = argparse.ArgumentParser(description="Compute the GC content "+
				"from each read from the input file and find the read with the highest GC content.")
	parser.add_argument("--i",help="Path to the input file. "+
						"The input file shall have the read name in a line that "+
						"begins with '>', followed by the read sequence in the next line.",
						type=str,required=True)
	return parser.parse_args()

def main():
	args = parse_arg()
	if os.path.isfile(args.i):
		with open(args.i) as input_file:
			in_file_list = input_file.read().splitlines()
			(highest_gc_name,highest_gc_pct) = find_read_with_most_gc(in_file_list)
			print(highest_gc_name)
			print(highest_gc_pct)
	else:
		print("Error: The specified input is not a file.")


if __name__ == '__main__':
	main()