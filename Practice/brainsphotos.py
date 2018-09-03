n,m = map(int,raw_input().split())
s = set([])
for i in range(0,n) :
	x = set(raw_input().split())
	s = s.union(x)
if ('C' in s or 'M' in s or 'Y' in s) :
	print "#Color"
else :
	print "#Black&White"
