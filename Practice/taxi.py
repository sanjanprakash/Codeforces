n = int(raw_input())
x = list(map(int,raw_input().split()))

arr = [0] * 4
for i in x :
	arr[i - 1] += 1

ans = arr[3]
arr[3] = 0

ans += (arr[1]/2)
arr[1] -= ((arr[1]/2) * 2)

if (arr[0] <= arr[2]) :
	ans += arr[0]
	arr[2] -= arr[0]
	arr[0] = 0
	ans += arr[2]
	arr[2] = 0
	ans += sum(arr)

else :
	ans += arr[2]
	arr[0] -= arr[2]
	arr[2] = 0
	if (arr[0] % 4 == 0) :
		ans += (arr[0]/4)
		arr[0] = 0
		ans += arr[1]
	elif (arr[0] % 4 == 1 or arr[0] % 4 == 2) :
		ans += (arr[0]/4) + 1
	else :
		ans += (arr[0]/4) + 1
		if (arr[1] > 0) :
			ans += 1
		
print ans
