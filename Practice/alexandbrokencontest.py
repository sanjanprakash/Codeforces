R = lambda:map(int,raw_input().split())
x = ["Danil", "Olya", "Slava", "Ann", "Nikita"]
a = raw_input()
print "YES" if sum(a.count(i) for i in x) == 1 else "NO"
