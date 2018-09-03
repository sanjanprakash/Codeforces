n = input()
arr = map(int,raw_input().split())
count = [0] * 3
i = 0
ids = [[],[],[]]
for x in arr :
	count[x - 1] += 1
	ids[x - 1].append(i + 1)
	i += 1
if (min(count) == 0) :
	print "0"
else :
	p,m,pe = 0,0,0
	print min(count)
	for i in range(0,min(count)) :
		print ids[0][p],ids[1][m],ids[2][pe]
		p += 1
		m += 1
		pe += 1
