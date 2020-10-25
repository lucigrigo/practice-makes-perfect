#include <bits/stdc++.h>
using namespace std;
#define ll long long

void solve(int no_case, int N, int M, int S, int R,
           vector<pair<int, int> > streets,
           vector<pair<int, vector<int> > > stones_available,
           vector<pair<int, vector<int> > > recipes)
{

}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        int N, M, S, R;
        cin >> N >> M >> S >> R;
        vector<pair<int, int> > streets;
        vector<pair<int, vector<int> > > stones_available;
        vector<pair<int, vector<int> > > recipes;

        for (int j = 0; j < M; ++j)
        {
            int a, b;
            cin >> a >> b;
            streets.push_back(pair<int, int>(a, b));
        }

        for (int j = 0; j < N; ++j)
        {
            int k;
            cin >> k;
            vector<int> stones;
            for (int u = 0; u < k; ++u)
            {
                int b;
                cin >> b;
                stones.push_back(b);
            }
            stones_available.push_back(pair<int, vector<int> >(k, stones));
        }

        for (int j = 0; j < R; ++j)
        {
            int k;
            cin >> k;
            vector<int> recps;
            for (int u = 0; u < k; ++u)
            {
                int a;
                cin >> a;
                recps.push_back(a);
            }
            int p;
            cin >> p;
            recipes.push_back(pair<int, vector<int> >(p, recps));
        }

        solve(i, N, M, S, R, streets, stones_available, recipes);
    }
    return 0;
}
