n = input()
m,c = 0,0
for i in range(0,n) :
	bear,fr = map(int,raw_input().split())
	if (bear > fr) :
		m += 1
	elif (fr > bear) :
		c += 1
if (m > c) :
	print "Mishka"
elif (c > m) :
	print "Chris"
else :
	print "Friendship is magic!^^"
