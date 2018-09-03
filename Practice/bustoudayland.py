n = input()
arr = []
ans = -1
for i in range(0,n) :
	l = raw_input()
	if (l[0:2] == "OO" and ans == -1) :
		l = "++" + l[2:]
		ans = i
	elif (l[3:5] == "OO" and ans == -1) :
		l = l[:3] + "++"
		ans = i
	arr.append(l)
if (ans == -1) :
	print "NO"
else :
	print "YES"
	for i in range(0,n) :
		print arr[i]
