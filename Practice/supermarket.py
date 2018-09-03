n,m = map(int,raw_input().split())
a,b = map(int,raw_input().split())
min_cost = float(a)/float(b)
for i in range (n - 1) :
    a,b = map(int,raw_input().split())
    if (float(a)/float(b) < min_cost) :
        min_cost = float(a)/float(b)
print m * min_cost
