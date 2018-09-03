n = input()
prev = raw_input()
ans = 1
for i in range(0,n - 1) :
	curr = raw_input()
	if (prev[1] == curr[0]) :
		ans += 1
	prev = curr
print ans
