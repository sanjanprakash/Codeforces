def sum_dig(n) :
    ans = 0
    while (n > 0) :
        ans += n % 10
        n /= 10
    return ans

k = int(raw_input())
n,count = 19,1
while (count < n) :
    if (count == k) :
        break    
    n += 9
    if (sum_dig(n) == 10) :
        count += 1
    
print n
