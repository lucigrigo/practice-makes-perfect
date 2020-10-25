/*
	--- PARTIALLY WORKING
*/
#include <bits/stdc++.h>
using namespace std;
#define ll long long

class Toy {
public:
	int e;
	int r;
	int index;

	Toy(int ee, int rr, int ii) {
		e = ee;
		r = rr;
		index = ii;
	}
};

struct ToyOrder {
	bool operator() (const Toy &p, const Toy &q) {
		return (p.e + p.r) < (q.e + q.r);
	}
};
	

void solve(int n_case, int n, int e[], int r[]) {
	++n_case;
	priority_queue<Toy, vector<Toy>, ToyOrder> pq;
	int e_sum = 0;

	for(int i = 0; i < n; ++i) {
		int cur_e = e[i];
		e_sum += cur_e;
		int cur_r = r[i];
		Toy t(cur_e, cur_r, i);
		pq.push(t);
	}

	int removed = 0;
	int total_removed = 0;
	int max_time = e_sum;
	int cur_time = e_sum;
	while(!pq.empty()) {
		Toy t = pq.top();
		if(t.e + t.r <= e_sum) {
			cur_time += t.e;
		} else {
			cur_time -= t.e;
			++removed;
			e_sum -= t.e;
		}
		pq.pop();
		if(cur_time > max_time) {
			max_time = cur_time;
			total_removed = removed;
		}
	}

	if(removed < n) {
		cout << "Case #" << n_case << ": " << total_removed << " INDEFINITELY" << endl;
	} else {
		cout << "Case #" << n_case << ": " << total_removed << " " << max_time << endl;
	}
}

int main() {
	int T;
	cin >> T;
	for(int i = 0; i < T; ++i) {
		int e[100];
		int r[100];
		int n;
		cin >> n;
		
		for(int j = 0; j < n; ++j) {
			int a, b;
			cin >> a >> b;
			e[j] = a;
			r[j] = b;
		}

		solve(i, n, e, r);
	}
	return 0;
}