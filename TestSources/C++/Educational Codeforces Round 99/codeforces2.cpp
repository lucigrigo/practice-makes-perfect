#include <bits/stdc++.h>

using namespace std;
#define ll long long

void solve(ll pos[4][2]) {
	ll ans = 0;

	cout << ans << endl;
}

int main() {
	int T; cin >> T;
	while(T--) {
		ll pos[4][2];
		for(int i = 0; i < 4; ++i)
			cin >> pos[i][0] >> pos[i][1];
		solve(pos);
	}
	return 0;
}