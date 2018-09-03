n = input()
count = 1
while (n > 1) :
	if (n % 2 == 1) :
		count += 1
	n /= 2
print count
