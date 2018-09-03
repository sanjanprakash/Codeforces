n = int(raw_input())
for i in range(0,n) :
	s = raw_input()
	if (len(s) > 10) :
		ans = s[0] + str(len(s) - 2) + s[len(s) - 1]
		s = ans
	print s
