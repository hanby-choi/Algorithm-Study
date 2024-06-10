#include <iostream>
#include <string>
using namespace std;
int main(){
	int a, b, c, count[10] = {0, };
	cin >> a >> b >> c;
	string mul = to_string(a*b*c);
	for(int i=0; i<mul.length(); i++){
		count[mul[i] - '0']++;
	}	
	for(int i=0; i<10; i++){
		cout << count[i] << '\n';
	}
}