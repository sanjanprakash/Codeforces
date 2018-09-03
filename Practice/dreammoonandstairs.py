n,m = map(int,raw_input().split())
ans = n
tsteps = 0
osteps = n
flag = False
while (tsteps <= n/2) :
	if ((tsteps + osteps) % m == 0) :
		flag = True
		ans = min(ans,tsteps + osteps)
	tsteps += 1
	osteps -= 2
if (flag == False) :
	print "-1"
else :
	print ans
