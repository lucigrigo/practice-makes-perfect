#include <bits/stdc++.h>
using namespace std;
#define ll long long

void solve(int n_case, int n, vector<int> e, vector<int> r) {
	// TODO
}

int main() {
	int T;
	cin >> T;
	for(int i = 0; i < T; ++i) {
		vector<int> e;
		vector<int> r;
		int n;
		cin >> n;
		
		for(int j = 0; j < n; ++j) {
			int a, b;
			cin >> a >> b;
			e.push_back(a);
			r.push_back(b);
		}

		solve(i, n, e, e);
	}
	return 0;
}