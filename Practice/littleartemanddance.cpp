#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll mod = 1e9 + 7;
const ll inf = 1e15;
const int N = 1e6 + 6;
int n,q,b[N],t;
queue<int>even,odd,ans;
int main()
{
    scanf("%d%d",&n,&q);
    for(int i = 1; i <= n; i++)
    {
        if(i % 2)
            odd.push(i);
        else
            even.push(i);
    }
    int len,Lipoter = 1,flag = 1;
    for(int i = 1; i <= q; i++)
    {
        scanf("%d",&t);
        if(t == 1)
        {
            scanf("%d",&len);
            flag = (flag + len + n) % n;
            if(flag == 0)
                flag = n;
        }
        else
        {
            if(flag % 2){
                if(Lipoter == 0)
                {
                    even.push(even.front());
                    even.pop();
                }
                else 
                    Lipoter = 0;
            }
            else
            {
                if(Lipoter == 1)
                {
                    odd.push(odd.front());
                    odd.pop();
                }
                else
                    Lipoter = 1;
            }
            if (flag % 2)
                flag++;
            else 
                flag--;
            if(flag == 0)
                flag = n;
        }
    }
    if(Lipoter){
        while(!even.empty() && !odd.empty())
        {
            ans.push(odd.front());
            odd.pop();
            ans.push(even.front());
            even.pop();
        }
    }
    else
    {
        while(!even.empty()&&!odd.empty())
        {
            ans.push(even.front());
            even.pop();
            ans.push(odd.front());
            odd.pop();
        }
    }
    while(1)
    {
        if(ans.front() == 1)
            break;
        else
        {
            ans.push(ans.front());
            ans.pop();
        }
    }
    while(flag <= n)
    {
        b[flag++] = ans.front();
        ans.pop();
    }
    int cnt = 1;
    while(!ans.empty())
    {
        b[cnt++] = ans.front();
        ans.pop();
    }
    for(int i = 1; i <= n; i++)
        printf("%d ",b[i]);
    return 0;
}
