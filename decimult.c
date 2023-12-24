#include <stdio.h>

int main(void) {
	int m, n, c;
	const int a[] = {5, 3, 2}; //235
	const int b[] = {8, 8, 5, 7, 1, 1}; //117588
	#define M (sizeof(a)/sizeof(a[0]))
	#define N (sizeof(b)/sizeof(b[0]))
	int s[M + N];

	m = 0;

	while (m != (M + N)) {
		s[m] = 0;
		m = m + 1;
	}

	m = 0;
	n = 0;
	c = 0;

	while (m != M) {
		n = 0;
		while (n != N) {
			int z, r;
			z = c + a[m] * b[n] + s[m + n];
			r = z % 10;
			s[m + n] = r;

			if (z >= 10) c = (z - r)/10;
			else c = 0;

			n = n + 1;
		}
		s[m + n] = c;
		c = 0;
		m = m + 1;
	}

	m = M + N;
	while (m != 0) {
		m = m - 1;
		printf("%i", s[m]);
	}

	printf("\n");


	printf("Foo\n");
	return 0;

}