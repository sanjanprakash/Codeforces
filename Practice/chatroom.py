s = list(raw_input())
ref = ['h','e','l','l','o']
i = 0
while (i < len(s) and len(ref) != 0):
	if (s[i] == ref[0]) :
		ref.pop(0)
	i += 1

if (len(ref) == 0) :
	print "YES"
else :
	print "NO"
