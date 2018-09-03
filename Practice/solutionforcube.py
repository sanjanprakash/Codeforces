arr = map(int,raw_input().split())
i = 0
wrong,right = 0,0
w = []
while (i < 24) :
	if (len(set(arr[i:i + 4])) == 1) :
		right += 1
	elif (len(set(arr[i:i + 4])) == 2) :
		w.append(set(arr[i:i + 4]))	
		wrong += 1
	i += 4

t1 = set(frozenset(i) for i in w)
	
if (right == 2 and len(set(t1)) == 4) :
	print "YES"
else :
	print "NO"
