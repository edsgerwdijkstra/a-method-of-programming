#!/usr/bin/python3


def truth_time(f,n):
	"""How long does it take to check if a formula is a theorem via truth table

	Args:
		f:
			Frequency at which the machine can evaluate 1 boolen operator in
			units of Hz.
		n:
			The number of boolean variables in the formula.

	Returns:

	Raises:


	"""
	s = (2**n)
	t = (n/f) * s



	print("f = {} GHz, n = {} variables. t = {} seconds = {} days = {} years.".format(f/(10**9), n, t, t/(60*60*24), t/(60*60*24*365)))
	print("storage required = {} Gbytes".format(s/(8*2**30)))
def main():
	"""It me, main.

	Args:

	Returns:

	Raises:

	"""
	f = 10**9 * 4
	n = 64
	truth_time(f,n)

	f = 10**9 * 4
	n = 128
	truth_time(f,n)

if __name__ == "__main__":
	main()