n,m,a,b = map(int,raw_input().split())
if (m >= n and n * a > b) :
	print b
else :
	if ((b * (n/m)) + max(0,min(a * (n - ((n/m) * m)),b)) < a * n) :
		print (b * (n/m)) + max(0,min(a * (n - ((n/m) * m)),b))
	else :
		print a * n
