#include <bits/stdc++.h>
using namespace std;
#define ll long long

void solve(int n) {
	set<ll> values;
	for(int x = 1; x <= n; ++x) {
		int copy = x;
		ll up = copy;

		while(true) {
			if (copy % 10 != 0) {
				break;
			}
			copy = copy / 10;
		}
		ll down = copy;
		ll val = up / down;
		if(values.find(val) == values.end())
			values.insert(val);
	}
	cout << values.size() << endl;
}

int main() {
	int T;
	cin >> T;
	while(T--) {
		int n;
		cin >> n;
		solve(n);
	}
	return 0;
}