#include <iostream>
using namespace std;
int main(){
	int n, k;
	cin >> n >> k;
	int num1 = 1, num2 = 1;
	for(int i=1; i<k+1; i++){
		num1 *= n-i+1;
		num2 *= i;
	}
	cout << num1/num2;
}