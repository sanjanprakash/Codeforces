#include <iostream>

using namespace std;

int main ()
{
	long long int n, a, b, ans, x;
	cin >> n;
	while (n > 0)
	{
		cin >> a >> b;
		ans = 0;
		while (a != 0 && b != 0)
		{
			if (a > b)
			{
				x = a/b;
				ans += x;
				a -= x * b;
			}
			else if (b > a)
			{
				x = b/a;
				ans += x;
				b -= x * a;
			}
			else
			{
				ans++;
				a -= b;
			}
		}
		cout << ans << endl;
		n--;
	}
	return 0;
}
