#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int digits(ll n) {
	int no_digits = 0;

	while (n) {
		no_digits++;
		n /= 10;
	}

	return no_digits;
}

void solve(int case_no) {
	string curr_year;
	cin >> curr_year;

	ll len = curr_year.length();

	ll sz = 1;

	while (sz < len) {
		ll curr = 0;
		ll prev = -1;
		string ans;

		

		++sz;
	}
	printf("Case #%d: %s\n", case_no, ans.c_str());
}

int main() {
	ll T; int i = 1;
	cin >> T;
	while (T--) {
		solve(i++);
	}
	return 0;
}