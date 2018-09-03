d = raw_input()
ref = "qwertyuiopasdfghjkl;zxcvbnm,./'"

s = raw_input()
ans = []
if (d == "L") :
	for i in range(0,len(s)) :
		for j in range(0,len(ref)) :
			if (s[i] == ref[j]) :
				ans.append(ref[j + 1])
else :
	for i in range(0,len(s)) :
		for j in range(0,len(ref)) :
			if (s[i] == ref[j]) :
				ans.append(ref[j - 1])
print ''.join(ans)
