n,k = map(int,raw_input().split())
if (k <= (n + 1)/2) :
	print (2 * k) - 1
else :
	print (2 * (k - ((n + 1)/2)))
