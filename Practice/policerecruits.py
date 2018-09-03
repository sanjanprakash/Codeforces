n = input()
arr = map(int,raw_input().split())
ans,count = 0,0
for x in arr :
	if (x == -1) :
		if (count == 0) :
			ans += 1
		else :
			count -= 1
	else :
		if (count == 0) :
			count = x
		else :
			count += x
print ans
