n = input()
start = raw_input()
pas = raw_input()

ans = 0
for i in range(0,n) :
	a,b = int(start[i]),int(pas[i])
	ans += min(abs(a - b),10 + a - b,10 + b - a)
print ans
