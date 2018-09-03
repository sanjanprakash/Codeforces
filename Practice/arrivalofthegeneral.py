n = input()
arr = map(int,raw_input().split())
s = []
for x in arr :
	s.append(x)
s.sort()

big,small = s[len(s) - 1],s[0]

if (arr.index(big) > len(arr) - 1 - arr[::-1].index(small)) :
	ans = arr.index(big) + len(arr) - 1 - len(arr) + arr[::-1].index(small)
else :
	ans = arr.index(big) + len(arr) - 1 - len(arr) + arr[::-1].index(small) + 1
print ans
