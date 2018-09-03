n = input()
s = raw_input()
arr = []
arr.append(s[0])
for i in range(1,len(s)) :
	if (len(arr) == 0) :
		arr.append(s[i])
	else :
		if (arr[len(arr) - 1] == s[i]) :
			arr.append(s[i])
		else :
			arr.pop(len(arr) - 1)
print len(arr)
