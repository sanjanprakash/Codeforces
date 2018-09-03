a = list(raw_input())
b = list(raw_input())
a = a + b
a.sort()

c = list(raw_input())
c.sort()
if (a == c) :
	print "YES"
else :
	print "NO"
