s = raw_input()
ans = []
i = 0
while (i < len(s) - 3) :
	if (s[i:i + 3] == "WUB") :
		i += 3
	else :
		j = i
		while (s[j:j + 3] != "WUB" and j < len(s) - 3) :
			j += 1
		if (j == len(s) - 3 and s[j:j + 3] != "WUB") :
			j += 3
		ans.append(s[i:j])
		i = j
if (s[i:] != "WUB") :
	ans.append(s[i:])
for x in ans :
	print x,
