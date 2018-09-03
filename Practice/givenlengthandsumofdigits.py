m,s = map(int,raw_input().split())
s1 = s
if (9 * m < s) :
	print "-1 -1"
elif (s == 0) :
	if (m == 1) :
		print "0 0"
	else :
		print "-1 -1"
else :
	arr = [0] * m
	s -= 1
	for i in range(m - 1,0,-1) :
		if (s > 9) :
			arr[i] = 9
			s -= 9
		else :
			arr[i] = s
			s = 0
	arr[0] = s + 1
	small = ''.join(map(str,arr))
	large = ""
	for i in range(0,m) :
		if (s1 >= 9) :
			large += "9"
			s1 -= 9
		else :
			large += str(s1)
			s1 = 0
	if (s1 != 0) :
		print "-1 -1"
	else :
		print small,large
