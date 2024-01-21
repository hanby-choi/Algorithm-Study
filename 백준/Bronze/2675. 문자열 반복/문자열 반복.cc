#include <iostream>
#include <string>
using namespace std;

int main(){
	int r, t;
	cin >> t;
	while(t > 0){
		string sentence, ans;
		cin >> r >> sentence;
		for(int i = 0; i < sentence.length(); i++){
			for(int j = 0; j < r; j++){
				ans += sentence[i];
			}
		}
		cout << ans << '\n';
		t--;
	}
}