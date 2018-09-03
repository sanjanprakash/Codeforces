def Fact(n) :
	if (n == 0 or n == 1) :
		return 1
	else :
		return (n * Fact(n - 1))
		
def nCr(n,r) :
	return (Fact(n)/(Fact(r) * Fact(n - r)))

n,k = map(int,raw_input().split())
arr = [1,0,1,2,9]
ans = 0

for i in range (0,k + 1) :
	ans += (nCr(n,i) * arr[i])
	
print ans
