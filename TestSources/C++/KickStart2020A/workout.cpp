#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int mxN = 1e6;

void solve(int no_case, int n, int k, int v[mxN])
{
    ++no_case;
    
}

int main()
{
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        int n, k;
        cin >> n >> k;
        int v[mxN];
        for (int j = 0; j < k; ++j)
        {
            cin >> v[j];
        }
        solve(i, n, k, v);
    }

    return 0;
}