k,r = map(int,raw_input().split())
arr = []
if (k % 10 == 0) :
	print "1"
else :
	flag = False
	for i in range(1,10) :
		arr.append((i * k) % 10)
		if ((i * k) % 10 == 0) :
			flag = True
			break
	if (flag == True) :
		if (r in arr) :
			print min(i,arr.index(r) + 1)
		else :
			print i
	else :
		print arr.index(r) + 1
