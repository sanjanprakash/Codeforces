n = input()
i = 1
arr = ["Sheldon","Leonard","Penny","Rajesh","Howard"]
while (5 * ((2 ** i) - 1) < n) :
	i += 1
n = (n - (5 * ((2 ** (i - 1)) - 1)) - 1)/(2 ** (i - 1))
print arr[n]
