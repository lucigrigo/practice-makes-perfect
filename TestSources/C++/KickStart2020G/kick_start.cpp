#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int mxN = 1e5;

int T;
int ans[mxN];
int l[mxN];
string  s[mxN];
int x;

void solve(int i) {
    for(int j = 0; j < s[i].length(); ++j) {
        if(s[i].length() - j <= 3)
            break;

        if(s[i][j] == 'K' && s[i][j + 1] == 'I'
            && s[i][j + 2] == 'C' && s[i][j + 3] == 'K') {
                x++;
                j += 3;
            }
        if(s[i][j] == 'S' && s[i][j + 1] == 'T'
            && s[i][j + 2] == 'A' && s[i][j + 3] == 'R'
            && s[i][j + 4] == 'T') {
                ans[i] += x;
                j += 4;
            }
    }
}

int main() {
    cin >> T;

    for(int i = 0; i < T; ++i) {
        cin >> s[i];
        solve(i);
        cout << "Case #" << i + 1 << ": " << ans[i] << endl;
    }

    return 0;
}
