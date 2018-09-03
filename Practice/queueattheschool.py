n,t = map(int,raw_input().split())
s = list(raw_input())
while (t > 0) :
	i = 0
	while (i < n - 1) :
		if (s[i] == 'B' and s[i + 1] == 'G') :
			s[i],s[i + 1] = s[i + 1],s[i]
			i += 2
		else :
			i += 1
	t -= 1

s = ''.join(s)
print s
