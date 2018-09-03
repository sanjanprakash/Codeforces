n,t = map(int,raw_input().split())
arr = map(int,raw_input().split())
curr = 0
while (curr < t - 1) :
	curr += arr[curr]
if (curr == t - 1) :
	print "YES"
else :
	print "NO"
