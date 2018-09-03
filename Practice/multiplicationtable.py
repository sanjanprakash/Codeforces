import math

n,x = map(int,raw_input().split())
count = 0
for i in range(1,int(math.sqrt(x)) + 1) :
	if (i <= n and x % i == 0 and x/i <= n) :
		count += 1
		if (x/i > math.sqrt(x)) :
			count += 1
print count
