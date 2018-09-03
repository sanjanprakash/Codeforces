n = int(raw_input())
arr = map(int,raw_input().split())
ans = []
for i in range(1,n + 1) :
	ans.append(arr.index(i) + 1)
for x in ans :
	print x,
