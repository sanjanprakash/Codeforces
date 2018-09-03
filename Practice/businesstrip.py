k = input()
g = map(int,raw_input().split())
g.sort()
if (k == 0) :
	print k
else :
	i = 11
	ans = 0
	while (ans < k and i >= 0) :
		ans += g[i]
		i -= 1
	if (ans < k) :
		print "-1"
	else :
		print 12 - i - 1
