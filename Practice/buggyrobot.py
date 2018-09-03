n = input()
s = raw_input()
u,d,l,r = 0,0,0,0
for x in s :
	if (x == 'L') :
		l += 1
	elif (x == 'D') :
		d += 1
	elif (x == 'U') :
		u += 1
	else :
		r += 1
ans = 2 * (min(u,d) + min(l,r))
print ans
