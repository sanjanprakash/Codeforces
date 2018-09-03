import math

def Check(n) :
	n = str(n)
	if ('0' in list(n) or '1' in list(n) or '2' in list(n) or '3' in list(n) or '5' in list(n) or '6' in list(n) or '8' in list(n) or '9' in list(n)) :
		return False
	return True

n = int(raw_input())
div = []
for i in range(1,int(math.sqrt(n)) + 1) :
	if (n % i == 0) :
		div.append(i)
		div.append(n/i)
		
ans = False
for x in div :
	if (Check(x) == True) :
		ans = True
		break

if (ans == True) :
	print "YES"
else :
	print "NO"
