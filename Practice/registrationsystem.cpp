#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
	int n;
	string temp;
	map <string,int> dict;
	cin >> n;
	while (n > 0) {
		cin >> temp;
		if (dict[temp] == 0)
			cout << "OK\n";
		else
			cout << temp << dict[temp] << endl;
		dict[temp]++;
		n--;
	}
	return 0;
}
