n,m = map(int,raw_input().split())
ans = 0
ans += (n/m) * m
while ((n/m) + (n % m) >= m) :
	n = (n/m) + (n % m)
	ans += (n/m) * m
ans += (n/m) + (n % m)
print ans
