arr = map(int,raw_input().split())
l = arr[1:]
l.sort()
ans = [0] * (arr[0] + 2)
ans[0] = -99999999
ans[1] = 0
for i in range(2,arr[0] + 2) :
	ans[i] = 1 + max(ans[max(0,i - l[0])],ans[max(0,i - l[1])],ans[max(0,i - l[2])])
print ans[arr[0] + 1]
