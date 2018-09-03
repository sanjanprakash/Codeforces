n,h = map(int,raw_input().split())
arr = map(int,raw_input().split())
ans = n
for i in arr :
	if (i > h) :
		ans += 1
print ans
