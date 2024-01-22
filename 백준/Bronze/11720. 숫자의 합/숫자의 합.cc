#include <iostream>
#include <string>
using namespace std;
int main(){
    int n;
    string num;
    cin >> n >> num;
    int total = 0;
    for(int i=0; i<n; i++){
        total += num[i] - '0';
    }
    cout << total;
}