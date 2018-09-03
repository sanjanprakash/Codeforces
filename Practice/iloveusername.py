n = input()
arr = map(int,raw_input().split())
big,small = arr[0],arr[0]
count = 0
for x in arr[1:] :
	if (x < small) :
		small = x
		count += 1
	elif (x > big) :
		big = x
		count += 1
print count
