n = int(raw_input())
x,y,z = 0,0,0
for i in range(0,n) :
	p,q,r = map(int,raw_input().split())
	x += p
	y += q
	z += r
	
if (x == 0 and y == 0 and z == 0) :
	print "YES"
else :
	print "NO"
