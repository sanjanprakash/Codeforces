n = input()
arr = map(int,raw_input().split())
f_eve,f_odd = -1,-1
c_eve,c_odd = 0,0
for i in range(0,n) :
	if (arr[i] % 2 == 0) :
		if (f_eve == -1) :
			f_eve = i
		c_eve += 1
	else :
		if (f_odd == -1) :
			f_odd = i
		c_odd += 1
if (c_eve == 1) :
	print f_eve + 1
else :
	print f_odd + 1
