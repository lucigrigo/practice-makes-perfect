#include <bits/stdc++.h>
using namespace std;
#define ll long long
const int mxN = 1e6;

int T;
int W[mxN], N[mxN], ans[mxN];
ll v[mxN][mxN];

void compute(int i) {
	int avg = 0;
	for(int j = 0; j < N[i]; ++j) {
		avg += v[i][j];
	}
	avg /= N[i];
	for(int j = 0; j < N[i]; ++j){
		ans[i] += abs(v[i][j] - avg);
	}
}

int main() {
	cin >> T;

	for(int i = 0; i < T; ++i) {
		cin >> N[i] >> W[i];
		for(int j = 0; j < N[i]; ++j) {
			cin >> v[i][j];
		}
	}

	for(int i = 0; i < T; ++i) {
		compute(i);
	}

	for(int i = 0; i < T; ++i) {
		cout << "Case #" << i + 1 << ":" << ans[i] << endl;
	}

	return 0;
}
