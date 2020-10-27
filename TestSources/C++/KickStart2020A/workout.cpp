#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ar array
const int mxN = 1e6;

void solve(int no_case, int n, int k, int v[mxN])
{
    ++no_case;
    int l = 1;
    int r = v[n - 1] - v[0];

    while(l < r) {
    	int m = (l + r) / 2;
    	int k2 = 0;
    	for(int i = 1; i < n; ++i) {
    		int d = v[i] - v[i - 1];
    		k2 += (d + m - 1) / m -1;
    	}
    	if(k2 <= k)
    		r = m;
    	else
    		l = m + 1;
    }

    cout << "Case #" << no_case << ": " << l << endl;
}

int main()
{
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        int n, k;
        cin >> n >> k;
        int v[n];
        for (int j = 0; j < n; ++j)
        {
            cin >> v[j];
        }
        solve(i, n, k, v);
    }

    return 0;
}