arr = map(int,raw_input().split())
s = sum(arr)
if (s == 0) :
	print "-1"
else :
	if (s % 5 == 0) :
		print s/5
	else :
		print "-1"
