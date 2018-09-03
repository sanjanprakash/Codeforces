r,c = 0,0
for i in range(0,5) :
	curr = map(int,raw_input().split())
	for j in range(0,5) :
		if (curr[j] == 1) :
			r,c = i,j
			
print abs(2- r) + abs(2 - c)
