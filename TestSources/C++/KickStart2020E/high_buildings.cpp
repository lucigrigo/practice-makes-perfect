#include <bits/stdc++.h>
using namespace std;
#define ll long long

void solve(int no_case, int n, int a, int b, int c) {
	no_case += 1;
	if(a + b - c > n) {
		cout << "Case #" << no_case << ": IMPOSSIBLE" << endl;
		return;
	}
	int only_left_vis = a - c;
	int only_right_vis = b - c;
	int remaining_non_vis = n - a - b + c;

	int min_h = n / 2 - 1;
	int max_h = n / 2 + 1;
	int med_h = n / 2;

	int ans[100];

	if(c == 1 && a + b - c != n) {
		if(a == 1 && b == 1) {
			cout << "Case #" << no_case << ": IMPOSSIBLE" << endl;
			return;
		} 
		if(a > 1 || b > 1) {
			int l = 0;
			int r = n - 1;
			while(only_left_vis > 0) {
				--only_left_vis;
				ans[l++] = med_h;
			}
			while(only_right_vis > 0) {
				--only_right_vis;
				ans[r--] = med_h;
			}
			if(a == 1) {
				ans[l] = max_h;
				for(int i = 1; i <= r; ++i) 
					ans[i] = min_h;
			} else {
				ans[r] = max_h;
				for(int i = l; i < r; ++i) 
					ans[i] = min_h;
			}
		}
	} else if (c > 1 || (c == 1 && a + b - c == n)) {
		int l = 0;
		int r = n - 1;
		while(only_left_vis > 0) {
			--only_left_vis;
			ans[l++] = min_h;
		}
		while(only_right_vis > 0) {
			--only_right_vis;
			ans[r--] = min_h;
		}
		ans[r] = ans[l] = max_h;
		int i;
		for(i = l + 1; remaining_non_vis > 0; ++i, --remaining_non_vis)
			ans[i] = min_h;
		for(; i < r; ++i)
			ans[i] = max_h;
	} else {
		cout << "Case #" << no_case << ": IMPOSSIBLE" << endl;
		return;	
	}
	cout << "Case #" << no_case << ": ";
	for(int i = 0; i < n; ++i) {
		cout << ans[i] << " ";
	}
	cout << endl;
}

int main() {
	int T; cin >> T;
	for(int i = 0; i < T; ++i) {
		int N, A, B, C;
		cin >> N >> A >> B >> C;
		solve(i, N, A, B, C);
	}
	return 0;
}