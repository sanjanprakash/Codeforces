n = input()
ans = "I hate "
if (n == 1) :
	ans += "it"
else :
	for i in range(2,n + 1) :
		if (i % 2 == 0) :
			ans += "that I love "
		else :
			ans += "that I hate "
	ans += "it"
	
print ans
