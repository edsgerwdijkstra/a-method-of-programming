#include <assert.h>
#include <stdio.h>

/*
AMOP pg 81

The minimal segment sum.

Testing Dijkstra's solution :P, how dare I!!!

Test cases

# Not 0






*/

#define NMAX 8

int minsegsum(int f[], int N) {
	int x = 0, y = 0, n = 0;
	assert(f != NULL);
	assert(N >= 0);
	assert(N <= NMAX);

	while (n != N) {
		assert(x <= 0); // obvious invariant
		y = y + f[n];

		if (y >= 0)
			y = 0;
		else if (y < 0) {
			if (x <= y)
				;
			else if (x > y)
				x = y;
		}
		n = n + 1;
	}

	return x;
}

struct testcase {
	int f[NMAX];
	int N;
	int a; // correct answer
};

void pri (struct testcase *t) {
	int i = 0;

	if (t->N == 0)
		printf("f[0] = (empty)");

	while (i != t->N) {
		if (i == 0)
			if (t->N != 1)
				printf("f[%d] = %d, ", t->N, t->f[i]);
			else
				printf("f[%d] = %d", t->N, t->f[i]);
		else if (i + 1 != t->N)
			printf("%d, ", t->f[i]);
		else
			printf("%d", t->f[i]);
		i = i + 1;
	}

	printf("\n");
}

int main (void) {
	struct testcase t[] = {
		{{1, 2, 3, 4, 5, 6, 7/*end*/}, /*N*/7, /*ANS*/0},
		{{1, 2, 3, 4, 5, 6, 7, 8/*end*/}, /*N*/8, /*ANS*/0},
		{{/*end*/}, /*N*/0, /*ANS*/0},
		{{7/*end*/}, /*N*/1, /*ANS*/0},
		{{9, 2/*end*/}, /*N*/2, /*ANS*/0},
		{{1, 2, 3, 4, -5, 6, 7/*end*/}, /*N*/7, /*ANS*/-5},
		{{1, 2, 3, 4, -5, -6, 7/*end*/}, /*N*/7, /*ANS*/-11},
		{{1, 2, 3, -4, -5, -6, 7/*end*/}, /*N*/7, /*ANS*/-15},
		{{1, -2, -3, -4, 5, 6, 7, 8/*end*/}, /*N*/8, /*ANS*/-9},
		{{-1, 2, 3, 4, 5, 6, 7, -8/*end*/}, /*N*/8, /*ANS*/-8},
		{{-1, 2, 3, -4, 5, 6, 7, -8/*end*/}, /*N*/8, /*ANS*/-8},
		{{-1, 2, 3, -4, -5, 6, 7, -8/*end*/}, /*N*/8, /*ANS*/-9},
		{{-99, 0/*end*/}, /*N*/2, /*ANS*/-99},
		{{-7, -9/*end*/}, /*N*/2, /*ANS*/-16},
		{{9, -1, 2/*end*/}, /*N*/3, /*ANS*/-1},
		{{9, -1, -2/*end*/}, /*N*/3, /*ANS*/-3}
	};

	int n = 0, N = sizeof(t)/sizeof(t[0]);
	int r; // computed result

	while (n != N) {
		pri(&t[n]);

		r = minsegsum(t[n].f, t[n].N);

		printf("result = answer? %d = %d. %s.\n\n", r, t[n].a, (r == t[n].a)? "yes" : "no");

		n = n + 1;
	}

}