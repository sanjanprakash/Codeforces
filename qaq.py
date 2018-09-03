s = raw_input()
a_s,q_s = [],[]
ans = 0
for i in range(0,len(s) - 2) :
    for j in range(i + 1,len(s) - 1) :
        for k in range(j + 1, len(s)) :
            if (s[i] == 'Q' and s[j] == 'A' and s[k] == 'Q') :
                #print i,j,k
                ans += 1
print ans
