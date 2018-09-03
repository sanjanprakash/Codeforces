import math
def Prime(n) :
	for i in range(2,int(math.sqrt(n)) + 1) :
		if (n % i == 0) :
			return False
	return True

n = input()
if (n % 4 == 0) :
	print n/2,n/2
else :
	for i in range(4,n - 3) :
		if (Prime(i) == False and Prime((n - i)) == Prime(i)) :
			print i,n - i
			break
