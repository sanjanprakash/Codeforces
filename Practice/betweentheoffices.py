n = input()
s = raw_input()
win,loss = 0,0
for i in range(0,n - 1) :
	if (s[i] == 'S' and s[i + 1] == 'F') :
		win += 1
	elif (s[i] == 'F' and s[i + 1] == 'S') :
		loss += 1
if (win > loss) :
	print "YES"
else :
	print "NO"
