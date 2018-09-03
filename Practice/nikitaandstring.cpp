#include<bits/stdc++.h> 

#define ssync ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0)
#define F first
#define S second
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;
typedef long double ld;
template<typename T>
using vc = vector<T>;
template<typename T, typename X>
using pr = pair<T, X>;

const ll MOD = 1e9 + 7;
const ld PI = 3.14159265;

ll powerWithMod(ll base, ll exponent, ll modulus = LLONG_MAX)
{
	ll result = 1;
	base %= modulus;
	while(exponent > 0)
	{
		if(exponent % 2 == 1)
			result = (result * base) % modulus;
		exponent >>= 1;
		base = (base * base) % modulus;
	}
	return result;
}

ll modInverse(ll a, ll m = MOD)
{
	return powerWithMod(a, m - 2, m);
}

string s;
int ca[5555], cb[5555];

int main()
{
	ssync;
	cin >> s;
	for(int i = 1; i <= s.size(); i++)
	{
		ca[i] = ca[i - 1] + (s[i - 1] == 'a');
		cb[i] = cb[i - 1] + (s[i - 1] == 'b');
	}
	int ans = max(ca[s.size()], cb[s.size()]);
	for(int i = 0; i <= s.size(); i++)
	{
		for(int j = i; j <= s.size(); j++)
		{
			ans = max(ans, ca[i] + cb[j] - cb[i] + ca[s.size()] - ca[j]);
		}
	}
	cout << ans << "\n";
	return 0;
}
