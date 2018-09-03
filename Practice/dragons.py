s,n = map(int,raw_input().split())
arr = []
for i in range(0,n) :
	x,y = map(int,raw_input().split())
	arr.append((x,y))
arr = sorted(arr, key = lambda x: x[0])
count = 0
for i in range(0,n) :
	if (s > arr[i][0]) :
		s += arr[i][1]
	else :
		count += 1
		break
if (count == 0) :
	print "YES"
else :
	print "NO"
