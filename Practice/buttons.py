n = input()
t = n
a,b = 1,0
ans = 0
while (a <= t) :
	ans += (a * n) - b
	a += 1
	b += 1
	n -= 1
print ans
