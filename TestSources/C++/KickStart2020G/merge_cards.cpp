#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int mxN = 1e9;

int T;
int n[100];
int v[100][100];
int ans[100];

void solve(int i) {
    int D[100][100];

    for(int j = 0; j < n[i] - 1; ++j) {
        
    }

}

int main() {
    ios::sync_with_stdio(0);
    cin >> T;

    for(int i = 0; i < T; ++i) {
        cin >> n[i];
        for(int j = 0; j < n[i]; ++j) {
            cin >> v[i][j];
        }
    }

    for(int i = 0; i < T; ++i) {
        solve(i);
        cout << "Case #" << i + 1 << ": " << ans[i] << endl;
    }

    return 0;
}
