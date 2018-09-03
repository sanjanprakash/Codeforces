n,m = map(int,raw_input().split())
arr1 = map(int,raw_input().split())
arr2 = map(int,raw_input().split())
x = set(arr1).intersection(arr2)
if (len(x) > 0) :
	x = list(x)
	x.sort()
	print x[0]
else :
	arr1.sort()
	arr2.sort()
	if (arr1[0] < arr2[0]) :
		print (10 * arr1[0]) + arr2[0]
	else :
		print (10 * arr2[0]) + arr1[0]
