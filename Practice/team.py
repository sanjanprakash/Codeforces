n = int(raw_input())
ans = 0
for i in range(0,n) :
	p = list(map(int,raw_input().split()))
	if (sum(p) > 1) :
		ans += 1
		
print ans
