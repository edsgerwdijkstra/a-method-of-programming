import click


def square_root2(N):
	assert(N >= 0)

	a = 0
	b = 1
	d = 1

	while (b < N):
		b = 2 * b
		d = 2 * d

	while (b != a + 1):

		c = (a + b) // 2
		d = d // 2

		click.echo(f"a = {a:>{2}}. b = {b:>{2}}. c = {c:>{2}}. d = {d:>{2}}. b - a = {b - a:>{2}}. a + d = {a + d:>{2}}. a + b = {a + b:>{2}}. {(a + d) == c:>{2}}")

		if (a + d) * (a + d) <= N:
			a = (a + d)
		else:
			b = (a + d)

		click.echo(f"b - a = {b - a:>{2}}")

	click.echo(f"Done. a = {a}. b = {b}. c = {c}. d = {d}.")

def square_root(N):
	assert(N >= 0)

	a = 0
	b = 1
	d = 1

	while (b < N):
		b = 2 * b
		d = 2 * d

	while (b != a + 1):

		c = (a + b) // 2
		click.echo(f"a = {a}. b = {b}. c = {c}. d = {d}.")
		d = d // 2

		if c * c <= N:
			a = c
		else:
			b = c

	click.echo(f"Done. a = {a}. b = {b}. c = {c}. d = {d}.")

@click.command()
@click.argument('n', type=int)
def sqrt(n):
	click.echo("foo")
	square_root2(n)


if __name__ == "__main__":
	sqrt()