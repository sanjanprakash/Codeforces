s = raw_input()
if (len(s) == 1) :
	if (s[0].isupper() == 1) :
		s = s.lower()
	else :
		s = s.upper()
if (len(s) > 1) :
	if (s.upper() == s) :
		s = s.lower()
	elif (s[0].islower() == 1 and s[1:].upper() == s[1:]) :
		temp = s[0].upper() + s[1:].lower()
		s = temp
		
print s
