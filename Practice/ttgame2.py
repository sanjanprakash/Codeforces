k,a,b = map(int,raw_input().split())
if a < k and b < k:
    print -1
    exit(0)
rema,remb = a % k, b % k
if rema <= (k - 1) * (b/k) and remb <= (k - 1) * (a/k):
    print a/k + b/k
else:
    print -1
