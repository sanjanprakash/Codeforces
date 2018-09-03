s = raw_input()
count = 1
i = 1
while (i < len(s) and count < 7) :
	 if (s[i] == s[i - 1]) :
	 	count += 1
	 else :
	 	count = 1
	 i += 1

if (count != 7) :
	print "NO"
else :
	print "YES"
