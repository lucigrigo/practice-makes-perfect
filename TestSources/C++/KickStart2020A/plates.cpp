#include <bits/stdc++.h>
using namespace std;
#define ll long long

void solve(int no_case, int n, int k, int p, int v[50][30]) {
    ++no_case;

    int dp[51][1501];
    for(int i = 0; i <= 50; ++i) {
        for(int j = 0; j <= 1500; ++j) {
            dp[i][i] = 0;
        }
    }

    for(int i = 0; i < n; ++i) {
        memcpy(dp[i + 1], dp[i], sizeof(dp[0]));
        for(int j = 0, s = 0; j < k; ++j) {
            s += v[i][j];
            for(int u = 0; u + j + 1 <= p; ++u) {
                dp[i + 1][u + j + 1] = max(dp[i][u] + s, dp[i + 1][u + j + 1]);
            }
        }
    }

    cout << "Case #" << no_case << ": " << dp[n][p] << endl;
}

int main() {
    int T;
    cin >> T;

    for(int i = 0; i < T; ++i) {
        int n, k, p;
        cin >> n >> k >> p;
        int v[50][30];

        for(int j = 0; j < n; ++j) {
            for(int u = 0; u < k; ++u) {
                cin >> v[j][u];
            }
        }

        solve(i, n, k, p, v);
    }
    return 0;
}
