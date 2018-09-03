#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int n,k,temp,i;
	vector <int> X;
	cin >> n >> k;
	for (i = 0; i < n; i++) {
		cin >> temp;
		X.push_back(temp);
	}
	sort(X.begin(),X.end());
	int count = 0, comp = X[n - k];

	i = n - 1;

	while (i >= 0 && X[i] >= comp && X[i] > 0) {
		i--;
		count++;
	}
	cout << count << endl;
	return 0;
}
