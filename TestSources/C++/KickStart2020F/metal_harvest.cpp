#include <bits/stdc++.h>
using namespace std;
#define ll long long

void solve(int no_case, int n, int k, vector<pair<int, int> > ti) {
    int cur_end = -1;
    int cur_start = -1;
    int ans = 0;

    for(int i = 0; i < ti.size(); ++i) {
        if(cur_end <= ti[i].first) {
            ++ans;
            cur_start = ti[i].first;
            cur_end = cur_start + k;
        } else {
            if(cur_end < ti[i].second) {
                while(cur_end < ti[i].second) {
                    ++ans;
                    cur_start = cur_end;
                    cur_end += k;
                }
            }
        }
    }

    cout << "Case #" << no_case + 1 << ": " << ans << endl;
}

int main() {
  ios::sync_with_stdio(0);
  int T;
  cin >> T;

  for (int i = 0; i < T; ++i) {
    int k, n; cin >> n >> k;
    vector<pair<int, int> > ti;

    for(int j = 0; j < n; ++j) {
        int a, b; cin >> a >> b;
        ti.push_back(pair<int, int>(a, b));
    }

    sort(ti.begin(), ti.end());
    solve(i, n, k, ti);
  }

  return 0;
}
