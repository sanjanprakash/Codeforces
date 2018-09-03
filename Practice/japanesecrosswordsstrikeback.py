n,x = map(int,raw_input().split())
print "YES" if (sum(map(int,raw_input().split())) + n - 1 == x) else "NO"
