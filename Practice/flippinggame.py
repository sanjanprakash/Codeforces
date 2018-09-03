n = input()
x = map(int,raw_input().split())
arr = [0] * n
co,c = 0,0
if (x[0] == 0) :
	arr[0] = 1
else :
	co += 1
for i in range(1,n) :
	if (x[i] == 1) :
		co += 1
		if (arr[i - 1] > 0) :
			arr[i] = arr[i - 1] - 1
	else :
		arr[i] = arr[i - 1] + 1
if (co == n) :
	print n - 1
else :
	print co + max(arr)
