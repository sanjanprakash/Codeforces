n = input()
a = map(int,raw_input().split())
a = sum(a)
b = map(int,raw_input().split())
b.sort()
if (a <= b[n - 1] + b[n - 2]) :
	print "YES"
else :
	print "NO"
