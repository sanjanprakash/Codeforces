n,t = map(int,raw_input().split())
arr = map(int,raw_input().split())
i = 0
while (t > 0) :
	t -= (86400 - arr[i])
	i += 1
print i
