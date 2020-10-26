#include <bits/stdc++.h>
using namespace std;
#define ll long long

void solve(int no_case, int n, int b, vector<int> v)
{
    ++no_case;
    sort(v.begin(), v.end());
    int ans = 0;

    if(n > 0 && b < v[0]) {
        cout << "Case #" << no_case << ": " << ans << endl;
        return;
    }

    for(int i = 0; i < n; ++i) {
        if(b - v[i] < 0)
            break;
        b -= v[i];
        ++ans;
    }

    cout << "Case #" << no_case << ": " << ans << endl;
}

int main()
{
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        int n, b;
        cin >> n >> b;
        vector<int> v;
        for (int j = 0; j < n; ++j)
        {
            int a;
            cin >> a;
            v.push_back(a);
        }
        solve(i, n, b, v);
    }

    return 0;
}