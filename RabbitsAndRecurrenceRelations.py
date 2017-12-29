"""
	RabbitsAndRecurrenceRelations.py
"""

import argparse

def count_total_rabbits(n,k):
	"""
	Counts the total number of rabbit pairs after n month, 
		given that each reproductive-age rabbit produces a litter of k rabbit pairs.
	Return the total number of rabbit pairs as an int. 
	Param:
		n {int}	: The number of months.
		k {int} : The number of rabbit pairs that each reproductive-age rabbit produces.
	"""

	total = 0
	r_n1 = 1
	r_n2 = 1
	if n < 0 or k < 0:
		print("Error: n and k cannot be < 0.")
		return total
	for i in xrange(0,n):
		if i == 0:
			total = r_n1
		elif i == 1:
			total = r_n2
		else:
			offspring = r_n1*k
			# The total number of rabbits any given month 
			#	will contain the rabbits that were alive the previous month, 
			#	plus any new offspring. 
			total = r_n2 + offspring			
			r_n1 = r_n2
			r_n2 = total

	return total


def parse_arg():
	"""
	Parses the arguments.
	"""
	parser = argparse.ArgumentParser("Counts the total number of rabbit pairs after n month, "+
									"given that each reproductive-age rabbit produces a litter of "+
									"k rabbit pairs.")
	parser.add_argument("--n",help="The number of months",type=int,required=True)
	parser.add_argument("--k",help="The number of rabbit pairs that each reproductive-age rabbit produces.",
							type=int,required=True)
	return parser.parse_args()

def main():
	args = parse_arg()
	print(count_total_rabbits(args.n,args.k))

if __name__ == '__main__':
	main()