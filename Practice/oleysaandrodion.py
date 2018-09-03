n,t = map(int,raw_input().split())
if (n == 1 and t == 10) :
	print "-1"
else :
	print t * (10 ** (n - len(str(t))))
