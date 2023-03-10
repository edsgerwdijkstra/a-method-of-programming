#!/usr/bin/python3

from inspect import signature
import sympy

##
vals = [
	[False, False],
	[False, True],
	[True, False],
	[True, True]
	]

vals3 = [
	[False, False, False],
	[False, False, True],
	[False, True, False],
	[False, True, True],
	[True, False, False],
	[True, False, True],
	[True, True, False],
	[True, True, True]
	]

vals4 = [
	[False, False, False, False],
	[False, False, False, True],
	[False, False, True, False],
	[False, False, True, True],
	[False, True, False, False],
	[False, True, False, True],
	[False, True, True, False],
	[False, True, True, True],
	[True, False, False, False],
	[True, False, False, True],
	[True, False, True, False],
	[True, False, True, True],
	[True, True, False, False],
	[True, True, False, True],
	[True, True, True, False],
	[True, True, True, True]
]

def f20(P, Q):
	"""
	the brackets in this formula are irrelevant
	"""
	return (not (P == Q)) == ((not P) == Q)

def f21(P, Q):
	return (P and Q) == ((P or (not Q)) and Q)

def myf21(P, Q):
	return (Q and (P or (not Q))) == ((Q and P) or (Q and (not Q)))

def f22(P, Q):
	return (P or Q) == ((P and (not Q)) or Q)

def f23(P, Q, R):
	return ((P == Q) or R) == ((P or R) == (Q or R))

def f24(P, Q):
	return ((P and Q) == P) == (Q == (P or Q))

def f25(P, Q, R):
	return ((P == Q) or (not R)) == ((P and R) == (Q and R))

def f26(P, Q):
	#return ((not P) or Q) == ((P and Q) == Q) # error in book
	return ((not P) or Q) == ((P or Q) == Q)

def f27(P, Q):
	return ((not P) or Q) == ((P and Q) == P)

def e1f1(P, Q):
	return f26(P, Q)

def e1f2(P, Q):
	return f27(P, Q)

def f28(P, Q):
	return (P == Q) == (((not P) or Q) and ((not Q) or P))

def e2(P, Q):
	return (P == Q) == ((P and Q) or (P and Q)) # definitely not valid

def e3(P, Q, R):
	return ((P or Q) and (P or R)) == ((P and Q) or (P and R))

def implies(P, Q):
	return ((not P) or Q)

def f29(P, Q):
	return (implies(P, Q)) == ((P and Q) == P)

def f30(P, Q):
	return (implies(P, Q)) == ((not P) or Q) # VALID, "by definition"

def f31(P, Q):
	return (implies(P, Q)) == ((P or Q) == Q)

def f32(P, Q):
	return ((P == Q)) == ((implies(P, Q)) and (implies(Q, P)))

def e4f1(P, Q, R):
	return ((implies(P, Q)) or R) == (implies((P or R), (Q or R)))

def e4f2(P, Q, R):
	return ((implies(P, Q)) or (not R)) == (implies((P and R), (Q and R)))

def f38(P, Q, R):
	return implies(implies(P, Q), implies(P or R, Q or R))

def e6f1(P, Q):
	return ((P and Q) == False) == ((not P) or (not Q))

def e6f2(P, Q):
	return (P and Q) == (((not P) and (not Q)) == (P == (not Q)))

def e6f3(P, Q, R):
	return ((P and R) == (Q and R)) == (((not P) and R) == ((not Q) and R))

def e6f4(P, Q, R):
	return ((P or R) == (Q or R)) == (((not P) or R) == ((not Q) or R))

def e7f1(P, Q, R):
	return (((not P) or Q) and ((not Q) or R) and P and (not R)) == False

def e7f2(P, Q, R, S):
	return (P and Q) or (R and S) or (not P)  or (not R) or (not (Q or S))

def e7f3(P, Q):
	return (not P) or Q or ((P or Q) and ((not P) or (not Q)))

def e7f4(P, Q, R):
	return ((P and Q) or (Q and R) or (R and P)) == ((P or Q) and (Q or R) and (R or P))

def e8f1(P, Q):
	return implies((P == Q), implies(P, Q))

def e8f2(P, Q, R):
	return implies(implies(P, Q), implies((P and R), (Q and R)))

def e8f3(P, Q, R):
	return (R and implies(P, Q)) == implies(((not R) or P), (R and Q))

def e8f4(P, Q, R):
	return implies((P and Q), R) == implies(P, ((not Q) or R))

#################################### My quantifier checks ######################

def rx(x):
	return ((x % 3) == 0)

def fx(x):
	return ((x % 2) == 0)# sympy.isprime(x)

def sx(x):
	return ((x % 5) == 0)

def Aleft0(x):
	if rx(x):
		return fx(x)
	else:
		return True

def Aright0(x):
	return ((not rx(x)) or fx(x))

def Ax0(): # A, trading p.c.77
	r = []
	for x in range(1, 100):
		if x == 1:
			P = Aleft0(x)
			Q = Aright0(x)
		else:
			P = (P and  Aleft0(x)) # generalization conjunction
			Q = (Q and  Aright0(x))
		R = (P == Q)

	r.append(R)
	is_validf(__name__, r)

def Aleft1(x):
	if rx(x) and sx(x):
		return fx(x)
	else:
		return True

def Aright1(x):
	if rx(x):
		return ((not sx(x)) or fx(x))
	else:
		return True

def Ax1(): # (42a)
	r = []
	for x in range(1, 100):
		if x == 1:
			P = Aleft1(x)
			Q = Aright1(x)
		else:
			P = (P and  Aleft1(x)) # generalization conjunction
			Q = (Q and  Aright1(x))
		R = (P == Q)

	r.append(R)
	is_validf(__name__, r)


def Aleft2(x):
	if rx(x):
		return fx(x)
	else:
		return True

def Aright2(x):
	if rx(x):
		return (fx(x) or sx(x))
	else:
		return True

def Ax2(): # (43a)
	r = []
	for x in range(1, 100):
		if x == 1:
			P = Aleft2(x)
			Q = Aright2(x)
		else:
			P = (P and  Aleft2(x)) # generalization conjunction
			Q = (Q and  Aright2(x))
		R = implies(P, Q)

	r.append(R)
	is_validf(__name__, r)

def Eleft0(x):
	if rx(x) and sx(x):
		return fx(x)
	else:
		return False

def Eright0(x):
	if rx(x):
		return (sx(x) and fx(x))
	else:
		return False

def Ex0(): # (42b)
	r = []
	for x in range(1, 100):
		if x == 1:
			P = Eleft0(x)
			Q = Eright0(x)
		else:
			P = (P or  Eleft0(x)) # generalization disjunction
			Q = (Q or  Eright0(x))
		R = (P == Q)

	r.append(R)
	is_validf(__name__, r)

def e9f1_left(x):
	if rx(x):
		return fx(x)
	else:
		return True

def e9f1_right(x):
	if rx(x):
		return (rx(x) and fx(x))
	else:
		return True

def e9f1():
	print(__name__)
	r = []
	for x in range(1, 100):
		if x == 1:
			P = e9f1_left(x)
			Q = e9f1_right(x)
		else:
			P = (P and  e9f1_left(x)) # generalization conjunction
			Q = (Q and  e9f1_right(x))

		R = (P == Q)
		print("| {:<6} | {:<6} | = {:<6}".format(repr(P), repr(Q), repr(R)))

	r.append(R)
	is_validf(__name__, r)


#################################### My checks #################################

def myf0(P, Q):
	return (not (Q == (not P))) == ((not Q) == (not P))
################################################################################

def boolfunc_argc(boolfunc):
	try:
		sig = signature(boolfunc)
	except Exception as ex:
		print("Exception getting number of arguments to function {}".format(ex))
		raise TypeError

	n = len(sig.parameters)

	assert (n == 2) or (n == 3) or (n == 4)

	return n

def is_validf(name, r):
	print(repr(r))
	for v in r:
		if not v:
			print("------------------------>{} is not a theorem (not valid)".format(name))
			break

def theoremX(num, boolfunc):
	if type(num) == int:
		name = "(" +  str(num) + ")"
	else: # non-integer names
		if not type(num) == str:
			raise TypeError
		name = "(" +  num + ")"

	print(name)

	r = []

	if boolfunc_argc(boolfunc) == 2:
		domain = vals
		for v in domain:
			P = v[0]
			Q = v[1]
			R = boolfunc(P, Q)
			r.append(R)
			print("| {:<6} | {:<6} | = {:<6}".format(repr(P), repr(Q), repr(R)))
	elif boolfunc_argc(boolfunc) == 3:
		domain = vals3
		for v in domain:
			P = v[0]
			Q = v[1]
			R = v[2]
			S = boolfunc(P, Q, R)
			r.append(S)
			print("| {:<6} | {:<6} | {:<6} | = {:<6}".format(repr(P), repr(Q), repr(R), repr(S)))
	elif boolfunc_argc(boolfunc) == 4:
		domain = vals4
		for v in domain:
			P = v[0]
			Q = v[1]
			R = v[2]
			S = v[3]
			T = boolfunc(P, Q, R, S)
			r.append(T)
			print("| {:<6} | {:<6} | {:<6} | {:<6} | = {:<6}".format(repr(P), repr(Q), repr(R), repr(S), repr(T)))
	else:
		raise TypeError

	is_validf(name, r)


def main():
	# theoremX(20, f20)
	# theoremX(21, f21)
	# theoremX("my (21)", f21)
	# theoremX(22, f22)
	# theoremX(23, f23)
	# theoremX(24, f24)
	# theoremX(25, f25)
	# theoremX(26, f26)
	# theoremX(27, f27)

	# theoremX("E1f1", e1f1)
	# theoremX("E1f2", e1f2)

	# theoremX(28, f28)

	# theoremX("E2", e2)
	# theoremX("E3", e3)

	# theoremX(29, f29)
	# theoremX(30, f30)
	# theoremX(31, f31)
	# theoremX(32, f32)

	# theoremX("E4f1", e4f1)
	# theoremX("E4f2", e4f2)

	# theoremX(38, f38)
	# theoremX("E6f1", e6f1)
	# theoremX("E6f2", e6f2)
	# theoremX("E6f3", e6f3)
	# theoremX("E6f4", e6f4)

	# theoremX("E7f1", e7f1)
	# theoremX("E7f2", e7f2)
	# theoremX("E7f3", e7f3)
	# theoremX("E7f4", e7f4)

	# theoremX("E8f1", e8f1)
	# theoremX("E8f2", e8f2)
	# theoremX("E8f3", e8f3)
	# theoremX("E8f4", e8f4)
################################################################################
	#theoremX("myf0", myf0)
	#Ax0()
	#Ax1()
	#Ax2()
	#Ex0()
	e9f1()

if __name__ == "__main__":
	main()