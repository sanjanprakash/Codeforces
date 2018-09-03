n = input()
arr = map(int,raw_input().split())
freq = [0] * 100001
for x in arr :
	freq[x] += 1
dp = [0] * 100001
dp[1] = freq[1]
M = 0
for i in range(2,100001) :
	M = max(dp[i - 2],M)
	if (freq[i] == 0) :
		dp[i] = max(M,dp[i - 1])
	else :
		dp[i] = (i * freq[i]) + M
		
print max(dp)
