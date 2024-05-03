#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int binarySearch(int n, int key, vector<int> &nums){
    int left = 0;
    int right = n-1;
    int mid;
    while (left <= right) {
        mid = (left + right) / 2;
        if (nums[mid] == key) {
            return 1;
        }
        else if (nums[mid] > key) {
            right = mid - 1;
        }
        else {
            left = mid + 1;
        }
    }
    return 0;
}

int main(void) {
    cin.tie(0); cout.tie(0);
    ios_base::sync_with_stdio(NULL);
    
    int n, m, key;
    cin >> n;
    vector<int> nums(n);
    for (int i=0; i<n; i++){
        cin >> nums[i];
    }
    sort(nums.begin(), nums.end()); // 입력 받은 숫자를 정렬
    cin >> m;
    while(m--) {
        cin >> key;
        cout << binarySearch(n, key, nums) << '\n'; // key가 있는지 없는지 확인 후 출력
    }
    return 0;
}
