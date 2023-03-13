#!/usr/bin/python3
import sys
import random
import math
import statistics
import os

def pigeon1(N):
	X = []
	for i in range(N):
		X.append(random.randint(1, 1000))

	print("N = %d" % N)
	print("X.i = {}".format(repr(X)))

	maxM = sum(X)
	print("maxM = sum(X.i) = %d" % maxM)
	M = maxM/random.randint(1, 10)

	print("N/2 = %f. M = %d" % (N/2, M))

	N_i = 0

	for x in X:
		if x >= M/N:
			print("{} >= {} (=M/N)".format(x, M/N))
			N_i = N_i + 1

	print("(N_i=) %d >= %f (=N/2). %r" % (N_i, N/2, (N_i >= N/2)))

	print("maxM=sum(X_i)=%d >= %f (=M). %r" % (maxM, M, maxM >= M))

	if (N_i >= N/2) and not (maxM >= M):
		print("!!!!!!!!!!!!!!!!!!!!!!!!NOT A THEOREM, << counter example!!!")
		exit(1)

	if (N_i == N) and not (maxM >= M):
		print("!!!!!!!!!!!!!!!!!!!!!!!!STRONGER NOT A THEOREM, << counter example!!!")
		exit(1)

	if (N_i == N):
		if not (maxM >= M):
			print("!!!!!!!!!!!!!!!!!!!!!!!!STRONGER AND EQUIVALENT NOT A THEOREM, << counter example!!!")
			exit(1)

def pigeon0(n):
	"""Dijkstra's formulation of the pigeon hole principle.

	No need to think about containers and distributing objects among them. It
	boils down to the maximum is at least the average and the minimum is at
	most the average. This function test the validity of this formulation of
	the pigeon hole principle for a sequence of length n of
	integers in randomly selected from the set [1, 1000]. The principle actually
	holds more generally for any finite bag of real numbers sequences of real
	numbers. A bag is a weakened notion of a set, a set, by definition contains
	only distinct elements, put another way, any element either occurs in the
	set once, or it does not occur at all. In constrast, a bag permits an
	element to occur 0, 1, or more times, so if d occurs in the bag, we can
	speak of the number of instances of d in the bag.

	Args:
		n:
			Length of the sequence to test.

	Returns:
		True if the pigeon principle holds for the sequence, False otherwise.

	Raises:

	"""
	numbers = []

	for i in range(n):
		numbers.append(random.randint(1, 1000))

	print(repr(numbers))
	avg = statistics.mean(numbers)
	mmax = max(numbers)
	mmin = min(numbers)
	print("avg = {}".format(statistics.mean(numbers)))
	print("max = {}, >= avg {} ? {}".format(mmax, avg, avg <= mmax))
	print("min = {}, <= avg {} ? {}".format(mmin, avg, mmin <= avg))

	return (avg <= mmax) and (mmin <= avg)

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
		pigeon1(random.randint(1, 1000))


	#pigeon0(10)


if __name__ == "__main__":
	main()