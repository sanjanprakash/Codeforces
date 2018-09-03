a = raw_input()
b = raw_input()
ans = ""
for i in range(0,len(a)) :
	if (a[i] == '1' and b[i] == '1') :
		ans += '0'
	elif (a[i] == '0' and b[i] == '1') :
		ans += '1'
	elif (a[i] == '1' and b[i] == '0') :
		ans += '1'
	else :
		ans += '0'
print ans
