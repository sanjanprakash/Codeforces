y = int(raw_input())
ans = False
while (ans != True) :
	y += 1
	if (len(set(list(str(y)))) == len(str(y))) :
		ans = True
		
print y
