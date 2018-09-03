n,m = map(int,raw_input().split())
s = map(int,raw_input().split())
s.sort()
ans = 10000

for i in range(0,m - n + 1) :
	if (s[i + n - 1] - s[i] < ans) :
		ans = s[i + n - 1] - s[i]
print ans
