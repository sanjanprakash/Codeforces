n = int(raw_input())
large = -1
ppl = 0
for i in range(0,n) :
	leave,enter = map(int,raw_input().split())
	ppl += enter - leave
	if (ppl > large) :
		large = ppl
		
print large
