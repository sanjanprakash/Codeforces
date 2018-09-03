n = input()
t = n
needs,cost = [],[]
ans,tot = 0,0
while (n > 0) :
	a,p = map(int,raw_input().split())
	needs.append(a)
	cost.append(p)	
	n -= 1
if (t == 1) :
	print (needs[0] * cost[0])
else :
	m = cost[0]
	for i in range(0,len(needs) - 1) :
		m = min(cost[i],m)
		if (cost[i] > cost[i + 1]) :
			ans += (tot + needs[i]) * m
			tot = 0
		else :
			tot += needs[i]
	if (cost[i + 1] >= m) :
		ans += (tot + needs[i + 1]) * m
	else :
		ans += (needs[i + 1] * cost[i + 1])
	print ans
