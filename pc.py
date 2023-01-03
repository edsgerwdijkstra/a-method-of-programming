#!/usr/bin/python3

from inspect import signature
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
	return ((implies(P, Q)) or R) == (implies((P and R), (Q or R)))

def e4f2(P, Q, R):
	return ((implies(P, Q)) or (not R)) == (implies((P and R), (Q and R)))

def boolfunc_argc(boolfunc):
	try:
		sig = signature(boolfunc)
	except Exception as ex:
		print("Exception getting number of arguments to function {}".format(ex))
		raise TypeError

	n = len(sig.parameters)

	assert (n == 2) or (n == 3)

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
	else:
		raise TypeError

	is_validf(name, r)


def main():
	theoremX(20, f20)
	theoremX(21, f21)
	theoremX("my (21)", f21)
	theoremX(22, f22)
	theoremX(23, f23)
	theoremX(24, f24)
	theoremX(25, f25)
	theoremX(26, f26)
	theoremX(27, f27)

	theoremX("E1f1", e1f1)
	theoremX("E1f2", e1f2)

	theoremX(28, f28)

	theoremX("E2", e2)
	theoremX("E3", e3)

	theoremX(29, f29)
	theoremX(30, f30)
	theoremX(31, f31)
	theoremX(32, f32)

	theoremX("E4f1", e4f1)
	theoremX("E4f2", e4f2)

if __name__ == "__main__":
	main()