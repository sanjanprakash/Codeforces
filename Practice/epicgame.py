def GCD(x,y) :
	while (y > 0) :
		x,y = y,(x % y)
	return x

a,b,n = map(int,raw_input().split())
count = 0
while (n > 0) :
	if (count % 2 == 0) :
		n -= GCD(a,n)
	else :
		n -= GCD(b,n)
	count += 1

if (count % 2 == 1) :
	print "0"
else :
	print "1"
