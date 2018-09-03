n = int(raw_input())
c = list(map(int,raw_input().split()))
s = sum(c)
c.sort(reverse = True)
ans,i = 0,0
while (ans <= s/2) :
	ans += c[i]
	i += 1
	
print i
