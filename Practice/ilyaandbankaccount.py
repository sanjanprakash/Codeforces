n = input()
if (n >= 0) :
	print n
else :
	x = list(str(n))
	y = list(str(n))
	l = len(x)
	x.pop(l - 1)
	y.pop(l - 2)
	x = ''.join(x)
	y = ''.join(y)
	if (int(x) > int(y)) :
		if (x == "-0") :
			print '0'
		else :
			print x
	else :
		if (y == "-0") :
			print '0'
		else :
			print y
