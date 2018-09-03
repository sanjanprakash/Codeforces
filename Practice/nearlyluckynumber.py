def Check(n) :
	n = set(list(str(n)))
	for x in n :
		if (x == '0' or x == '1' or x == '2' or x == '3' or x == '5' or x == '6' or x == '8' or x == '9') :
			return False
	return True

n = list((raw_input()))
count = 0
for x in n :
	if (x == '4' or x == '7') :
		count += 1
ans = Check(count)
if (ans == False) :
	print "NO"
else :
	print "YES"
