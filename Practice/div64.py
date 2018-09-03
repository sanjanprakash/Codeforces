x = raw_input()
flag = False
for i in range(0,len(x)) :
	if (x[i] == '1') :
		flag = True
		break
        
count = 0
for j in range(i,len(x)) :
	if (x[j] == '0') :
		count += 1
if (flag == True and count >= 6) :
	print "yes"
else :
	print "no"
