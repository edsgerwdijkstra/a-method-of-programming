"""
[w,g] -> XXX
[g,w] -> XXX
[g,c] -> XXX
[c,g] -> XXX
----
Dijkstra'solution , wolf and the cabbage are two alphas, the goat is a gamma.
On account of the symmetry WRT the goat, the goat
cannot be left with neither the wolf nor the cabbage. This gets you the generalized
solution in the sense that it eliminates the distinction between wolf and cabbage.
-----
e=empty
[w,g,c] - []
[w,c] g-> []
[w,c] <-e [g]
[c] w-> [g]
[c] <-g [w]
[g] c-> [w]
[g] <-e [w,c]
[] g-> [w,c]
[] - [g,w,c]
----
## swapping wolf and cabbage
[w,g,c] - []
[w,c] g-> []
[w,c] <-e [g]
[w] c-> [g]
[w] <-g [c]
[g] w-> [c]
[g] <-e [w,c]
[] g-> [w,c]
[] - [g,w,c]
----
// chat gpt solution 1
[w,g,c] - []
[w,c] g-> []
[w,c] <-e [g]
[c] w-> [g]
[c] <-g [w] // slightly ambiguous
[g] c-> [w] // slightly ambiguous
[g] <-e [c,w] // slightly ambiguous
[] g-> [c,w]
[] - [g,c,w]
----
// chat gpt solution 2
[w,g,c] - []
[w,g] c-> [] // XXX wolf eats goat


"""