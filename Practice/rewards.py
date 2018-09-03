a = map(int,raw_input().split())
b = map(int,raw_input().split())
n = input()
if (sum(a) % 5 == 0) :
	ans = sum(a)/5
else :
	ans = (sum(a)/5) + 1
if (sum(b) % 10 == 0) :
	ans += sum(b)/10
else :
	ans += (sum(b)/10) + 1
if (ans <= n) :
	print "YES"
else :
	print "NO"
