#include <bits/stdc++.h>
using namespace std;
#define ll long long

void solve(int no_case, int n, vector<int> v) {
    if(v.size() <= 1) return;
    int ans = 2;
    int dif = v[1] - v[0];
    int max_ans = ans;

    for(int i = 2; i < n; ++i) {
        int cur_dif = v[i] - v[i - 1];

        if(cur_dif == dif) {
            ++ans;
        } else {
            max_ans = max(max_ans, ans);
            ans = 2;
            dif = cur_dif;
        }
    }

    max_ans = max(max_ans, ans);
    cout << "Case #" << no_case + 1 << ": " << max_ans << endl;
}

int main() {
    int T;
    cin >> T;

    for(int i = 0; i < T; ++i) {
        int n;
        cin >> n;
        vector<int> v;

        for(int j = 0; j < n; ++j) {
            int a;
            cin >> a;
            v.push_back(a);
        }

        solve(i, n, v);
    }

    return 0;
}
