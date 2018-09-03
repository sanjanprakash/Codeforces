k,n,w = map(int,raw_input().split())
ans,cash = 0,0
for i in range(1,w + 1) :
	cash += (i * k)
	
if (n < cash) :
	ans += cash - n
print ans
