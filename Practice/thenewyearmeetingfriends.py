arr = map(int,raw_input().split())
arr.sort()
small = 30000
for i in range(arr[0],arr[2] + 1) :
	if (small > arr[2] - arr[0] + abs(i - arr[1])) :
		small = arr[2] - arr[0] + abs(i - arr[1])
print small
