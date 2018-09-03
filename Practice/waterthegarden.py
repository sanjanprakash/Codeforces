t = int(raw_input())

while (t > 0) :
    n,k = map(int,raw_input().split())
    arr = map(int,raw_input().split())
    ans = arr[0] - 1    
    if (k > 1) :
        if (n - arr[k - 1] > ans) :
            ans = n - arr[k - 1]
    else :
        ans = max(arr[0] - 1,n - arr[0])
    for i in range(0,k - 1) :
        if ((arr[i + 1] - arr[i])/2 > ans) :
            ans = (arr[i + 1] - arr[i])/2
    print ans + 1
    t -= 1
