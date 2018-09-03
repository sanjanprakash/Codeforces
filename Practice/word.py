s = raw_input()
up,down = 0,0
for i in range(0,len(s)) :
	if (s[i].islower() == True) :
		down += 1
	else :
		up += 1
if (up > down) :
	s = s.upper()
else :
	s = s.lower()
	
print s
