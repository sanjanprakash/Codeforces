n,k = map(int,raw_input().split())
while (5 * ((n * (n + 1))/2) + k > 240) :
	n -= 1
print n
