#include<iostream>

using namespace std;

int main() {
    long long int n,m;

    cin >> n >> m;
    long long int * arr = new long long int[m];
    for(long long int i = 0;i < m; i++) 
        cin >> arr[i];
    long long int cost;
    cost = 0;
    long long int curr = 1;
    for(long long int i = 0; i < m;i++){
        if(curr <= arr[i]){
            cost += arr[i] - curr;
        }
        else{
            cost += n - curr + arr[i];
        }
        curr = arr[i];

    }
    cout << cost << endl;
    return 0;
}
