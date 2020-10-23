#include <bits/stdc++.h>
using namespace std;
#define ll long long

void solve(int i, queue<pair<int, int> > q, int x, int n) {
  vector<int> ans;

  while (q.size() > 0) {
      pair<int, int> a = q.front(); q.pop();
      int amount = a.first;
      int index = a.second;
      if(amount <= x) {
          ans.push_back(index);
      } else {
          amount -= x;
          q.push(pair<int, int>(amount, index));
      }
  }

  cout << "Case #" << i << ": ";
  for(int j = 0; j < ans.size(); ++j) {
      cout << ans[j] + 1 << " ";
  }
  cout << endl;
}

int main() {
  ios::sync_with_stdio(0);
  int T;
  cin >> T;

  for (int i = 0; i < T; ++i) {
    queue<pair<int, int> > q;
    int x;
    int n;
    cin >> n >> x;
    for (int j = 0; j < n; ++j) {
      int a;
      cin >> a;
      q.push(pair<int, int>(a, j));
    }
    solve(i, q, x, n);
  }

  return 0;
}
