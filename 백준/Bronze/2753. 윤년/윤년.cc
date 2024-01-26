#include <iostream>
using namespace std;

int checkLap(int year){ // 4의 배수이자 100의 배수 x 또는 400의 배수
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0){
        return 1;
    } 
    return 0; 
}

int main(){
    int n;
    cin >> n;
    cout << checkLap(n);
}