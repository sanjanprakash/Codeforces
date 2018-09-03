k = int(raw_input())
l = int(raw_input())
m = int(raw_input())
n = int(raw_input())
d = int(raw_input())
count = 0
for i in range(1,d + 1) :
	if ((i % k == 0) or (i % l == 0) or (i % m == 0) or (i % n == 0)) :
		count += 1
		
print count
