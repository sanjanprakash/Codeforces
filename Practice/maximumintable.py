n = input()
arr = []
r = [1] * n
arr.append(r)
for i in range(1,n) :
	arr.append([1])
for i in range(1,n) :
	for j in range(1,n) :
		arr[i].append(arr[i - 1][j] + arr[i][j - 1])

print arr[n - 1][n - 1]
