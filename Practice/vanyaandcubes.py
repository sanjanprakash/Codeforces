n = input()
ans = 0
i = 1
while (ans < n) :
	ans += (i * (i + 1))/2
	i += 1
if (ans == n) :
	print i - 1
else :
	print i - 2
