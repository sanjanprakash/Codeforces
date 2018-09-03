n = input()
p = map(int,raw_input().split())
q = map(int,raw_input().split())
print "I become the guy." if len(set(p[1:] + q[1:])) == n else "Oh, my keyboard!"
