n,l = map(int,raw_input().split())
arr = map(int,raw_input().split())
arr = list(set(arr))
ans = -1
arr.sort()

i = 0
if (len(arr) == 1) :
	ans = max(arr[0],l - arr[0])
else :
	while (i < len(arr) - 1) :
		if (i == 0) :
			if (arr[i] != 0 and arr[i] > ans) :
				ans = arr[i]
			else :
				if ((arr[i + 1] - arr[i])/float(2) > ans) :
					ans = (arr[i + 1] - arr[i])/float(2)
		else :
			if ((arr[i + 1] - arr[i])/float(2) > ans) :
				ans = (arr[i + 1] - arr[i])/float(2)
		i += 1

	if (arr[i] != l) :
		if (l - arr[i] > ans) :
			ans = l - arr[i]
	else :
		if ((arr[i] - arr[i - 1])/float(2) > ans) :
			ans = (arr[i] - arr[i - 1])/float(2)
print ans
