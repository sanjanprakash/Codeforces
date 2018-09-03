n,k,x = map(int,raw_input().split())
arr = map(int,raw_input().split())

if (k == n) :
	print n * x
else :
	print sum(arr[0:n - k]) + k * x
