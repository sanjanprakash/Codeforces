n,k = map(int,raw_input().split())
arr = map(int,raw_input().split())
count = 0
for x in arr :
	if (5 - x >= k) :
		count += 1
print count/3
