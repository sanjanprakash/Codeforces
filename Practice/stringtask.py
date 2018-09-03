s = raw_input()
forbidden = ['a','e','i','o','u','y']
ans = ""

for i in range(0,len(s)) :
	x = s[i]
	x = x.lower()
	if (x not in forbidden) :
		ans += '.' + x

print ans
