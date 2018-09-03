pas = raw_input()
n = input()
words = []
flag = False
for i in range(0,n) :
	temp = raw_input()
	if (temp == pas or temp[::-1] == pas) :
		flag = True
		break
	words.append(temp)
if (flag == True) :
	print "YES"
else :
	count = 0
	found = []
	for i in range(0,n) :
		if (words[i][0] == pas[1]) :
			count += 1
			found.append(i)
	if (count == 0) :
		print "NO"
	else :
		flag = False
		for i in range(0,n) :
			if (words[i][1] == pas[0]) :
				if ([i] != found) :
		 			flag = True
		if (flag == True) :
			print "YES"
		else :
			print "NO"		
