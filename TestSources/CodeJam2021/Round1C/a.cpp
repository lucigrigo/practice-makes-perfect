#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(int case_no) {
	ll N, K; cin >> N >> K;
	unordered_set<ll> v;
	for (int i = 0; i < N; ++i) {
		ll n;
		cin>>n;
		v.insert(n);
	}

	double probs[K];
	double ans = 0.0;
	for (int i = 1; i <= K; ++i) {
		if (v.find(i) != v.end()) {
			probs[i] = 0.0;
		} else {
			int sz = 1;
			int x = 1;

			while (1) {
				if (i - sz - 1 < 1 || i + sz + 1 > K)
					break;
				if (v.find(i - sz - 1) == v.end() && v.find(i + sz + 1) == v.end()) {
					++x;
				} else
					break;
				++sz;
			}

			probs[i] = (double) x / (double) N;
		}
	}

	for (double prob : probs)
		ans = max(ans, prob);

	printf("Case #%d: %f\n", case_no, ans);
}

int main() {
	ll T; int i = 1;
	cin >> T;
	while (T--) {
		solve(i++);
	}
	return 0;
}