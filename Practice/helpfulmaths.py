x = raw_input()
arr = [0] * 3
for i in range(0,len(x)) :
	if (x[i] != '+') :
		if (x[i] == '1') :
			arr[0] += 1
		elif (x[i] == '2') :
			arr[1] += 1
		else :
			arr[2] += 1
			
ans = ""
count = 0
for i in range(0,3) :
	for j in range (0,arr[i]) :
		if (count < len(x) - 1) :
			ans += str(i + 1) + "+" 
			count += 2
		else :
			ans += str(i + 1)

print ans
