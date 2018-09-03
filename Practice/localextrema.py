n = int(raw_input())
num = map(int,raw_input().split())
ans = 0
for i in range(1,len(num) - 1) :
	if (num[i] < num[i - 1] and num[i] < num[i + 1]) :
		ans += 1
	if (num[i] > num[i - 1] and num[i] > num[i + 1]) :
		ans += 1
print ans
