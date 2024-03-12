#include <iostream>
using namespace std;
const int MAX = 26;  // n <= 10^7 

int bitCount(int n){
    int cnt = 0; // n = 10 -> 1010 0001 0010 0100 1000 &
    for (int i=0; i<MAX; i++){
        if (n & (1 << i)){ // 00100 i가 2일때 
            cnt++; 
        }
    }
    return cnt; 
}

int minCount(int n, int k){
    int required = 0; 
    while (true){
        if (bitCount(n+required) <= k) {
            return required;
        }
        required += 1;
    }
}

int main()
{
    // 입력 
    int n, k;
    cin >> n >> k;
    // 연산
    // 출력 
    cout << minCount(n, k);
    return 0; 
}