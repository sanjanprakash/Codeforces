n = int(raw_input())
arr = map(int,raw_input().split())
ans,count = 1,1
for i in range(0,len(arr) - 1) :
	if (arr[i] > arr[i + 1]) :
		if (count > ans) :
			ans = count
		count = 1
	else :
		count += 1
if (count > ans) :
	ans = count
print ans
