n = input()
h,a = [],[]
count = 0
for i in range(0,n) :
	p,q = map(int,raw_input().split())
	h.append(p)
	a.append(q)
	
for i in range(0,n) :
	for j in range(0,n) :
		if (h[i] == a[j]) :
			count += 1
print count
