#include <stdio.h>

int main() {
	int a, b;

	a = 5;
	b = 6;
	printf("5/6 = %d. 5%%6 = %d\n", a/b, a % b);
	a = -5;
	b = 6;
	printf("-5/6 = %d. -5%%6 = %d\n", a/b, a % b);
	a = 5;
	b = -6;
	printf("5/-6 = %d. 5%%-6 = %d\n", a/b, a % b);
	a = -5;
	b = -6;
	printf("-5/-6 = %d. -5%%-6 = %d\n", a/b, a % b);
	return 0;
}