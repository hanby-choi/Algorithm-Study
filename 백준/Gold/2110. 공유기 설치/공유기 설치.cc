#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int cntRouter(int dist, vector<int>& router){
    int cnt = 1;
    int cur = router[0];
    for (int i=1; i<router.size(); i++){
        if (router[i] - cur >= dist){
            cnt++;
            cur = router[i];
        }
    }
    return cnt;
}

int binarySearch(int left, int right, int target, vector<int>& router){
    while(left <= right){
        int mid = (left + right) / 2;
        int installed = cntRouter(mid, router);
        if (installed >= target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return left - 1;
}

int main(){
    int n, c;
    cin >> n >> c;
    vector<int> house(n, 0);
    for (int i=0; i<n; i++) {
        cin >> house[i];
    }
    sort(house.begin(), house.end());
    cout << binarySearch(1, house[n-1]-house[0], c, house);
    return 0;
}