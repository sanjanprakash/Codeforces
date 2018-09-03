m,n,a = map(int,raw_input().split())
ans = 0
if (m % a == 0) :
	ans = m/a
else :
	ans = (m/a) + 1
if (n % a == 0) :
	ans *= n/a
else :
	ans *= ((n/a) + 1)
	
print ans
