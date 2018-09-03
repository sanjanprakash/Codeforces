n = input()
while (n > 0) :
	t = input()
	if (360 % (180 - t) == 0) :
		print "YES"
	else :
		print "NO"
	n -= 1
