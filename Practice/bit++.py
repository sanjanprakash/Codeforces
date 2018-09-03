n = int(raw_input())
ans = 0

for i in range(0,n) :
	x = raw_input()
	if (x[1] == '+') :
		ans += 1
	else :
		ans -= 1

print ans
