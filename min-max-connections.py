#!/usr/bin/python3
import sys
import random
import math
import statistics
import os


def main():
	"""Main function

	What else would you like to know?

	Args:

	Returns:

	Raises:

	"""
	print(sys.version)

	random.seed(os.urandom(8))

	for i in range(0, 1000000):
		n = 10

		f = []
		for i in range(0, n):
			f.append(random.randint(-1000, 1000))

		m = max(f)
		nf = []
		for x in f:
			nf.append(-x + m)
		print("f = {}".format(f))
		print("-f+m = {}".format(nf))
		print("min = {}".format(min(nf)))
		if min(nf) != 0:
			print("nah!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			exit(1)
		#assert(min(nf) != 0)


if __name__ == "__main__":
	main()