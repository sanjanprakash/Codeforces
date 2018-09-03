n,m = map(int,raw_input().split())
for i in range(0,n) :
	line = []
	if (i % 2 == 0) :
		for j in range(0,m) :
			line.append('#')
		print "".join(line)
	else :
		if (i % 4 == 1) :
			for j in range(0,m - 1) :
				line.append('.')
			line.append('#')
			print "".join(line)
		else :
			line.append('#')
			for j in range(0,m - 1) :
				line.append('.')
			print "".join(line)
