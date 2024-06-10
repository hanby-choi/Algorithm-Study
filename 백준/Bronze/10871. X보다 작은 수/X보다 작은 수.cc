#include <iostream>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);	// 동기화 해제
	cin.tie(NULL);	// 묶음 해제
    int n, x, num;
    cin >> n >> x;
    for(int i=0; i<n; i++){
        cin >> num;
        if (num < x){
            cout << num << '\n';
        }
    }
}