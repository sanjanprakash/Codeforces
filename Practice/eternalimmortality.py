a,b = map(int,raw_input().split())
if (b/10 > a/10) :
	print "0"
else :
	ans = 1
	t = 0
	while (b != a) :
		ans *= (b % 10)
		b -= 1
	print ans % 10
