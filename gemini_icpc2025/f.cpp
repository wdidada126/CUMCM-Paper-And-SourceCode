// Copyright 2025 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// ==============================================================================

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <numeric>

using namespace std;

struct Cat {
    int id;
    int p;
    vector<int> likes;
};

struct Edge {
    int weight;
    int X;
    int P;
};

bool solve() {
    int N, M;
    if (!(cin >> N >> M)) return false;

    vector<Cat> cats(N);
    vector<vector<int>> cats_at_pot(M + 1);
    long long sum_K = 0;
    for (int i = 0; i < N; ++i) {
        cats[i].id = i;
        int k;
        cin >> cats[i].p >> k;
        cats[i].likes.resize(k);
        for (int j = 0; j < k; ++j) {
            cin >> cats[i].likes[j];
        }
        cats_at_pot[cats[i].p].push_back(i);
        sum_K += k;
    }

    // 1. Identify constrained and free pots.
    vector<bool> is_constrained(M + 1, false);
    int constrained_count = 0;
    for (int p = 1; p <= M; ++p) {
        if (!cats_at_pot[p].empty()) {
            is_constrained[p] = true;
            constrained_count++;
        }
    }

    // 2. Calculate P_max(X).
    // P_max(X) = max(Q-1) over cats at Q liking X. Initialized to 0.
    vector<int> P_max(M + 1, 0);
    for (const auto& cat : cats) {
        for (int x : cat.likes) {
            P_max[x] = max(P_max[x], cat.p - 1);
        }
    }

    // 3. Calculate I(P) and construct G'.
    // We calculate I(P) implicitly while constructing the edges of G'.
    vector<Edge> edges;
    for (int p = 1; p <= M; ++p) {
        if (!is_constrained[p]) continue;

        // Calculate I(P) using frequency counting.
        map<int, int> counts;
        for (int cat_idx : cats_at_pot[p]) {
            for (int x : cats[cat_idx].likes) {
                counts[x]++;
            }
        }

        int required_count = cats_at_pot[p].size();
        for (auto const& [x, count] : counts) {
            if (count == required_count) {
                // X is in I(P).
                // Check the constraint P >= S_X = P_max(X) + 1.
                if (p >= P_max[x] + 1) {
                    edges.push_back({P_max[x], x, p});
                }
            }
        }
    }

    // 4. Sort edges by weight descending.
    sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        return a.weight > b.weight;
    });

    // 5. Run greedy matching algorithm.
    vector<bool> pot_matched(M + 1, false);
    vector<bool> plant_matched(M + 1, false);
    vector<int> V_C; // Plants used for constrained pots.
    int matching_size = 0;

    for (const auto& edge : edges) {
        if (!plant_matched[edge.X] && !pot_matched[edge.P]) {
            plant_matched[edge.X] = true;
            pot_matched[edge.P] = true;
            V_C.push_back(edge.X);
            matching_size++;
        }
    }

    // 6. Check coverage of S_C.
    if (matching_size < constrained_count) {
        return false;
    }

    // 7. Check feasibility of the remaining problem.
    // Calculate counts of P_max(X) for R_U (remaining plants).
    vector<int> Count_RU(M + 1, 0); // Counts for P_max values 0..M.
    for (int x = 1; x <= M; ++x) {
        if (!plant_matched[x]) {
            Count_RU[P_max[x]]++;
        }
    }

    // Calculate prefix sums of available plants.
    // Prefix_RU[k] = sum of Count_RU[i] for i=0..k-1. (P_max < k)
    vector<long long> Prefix_RU(M + 2, 0);
    for (int k = 1; k <= M + 1; ++k) {
        Prefix_RU[k] = Prefix_RU[k-1] + Count_RU[k-1];
    }

    // Calculate demand. Demand[k] = number of free pots in {1..k}.
    vector<int> Demand(M + 1, 0);
    int free_pots_count = 0;
    for (int p = 1; p <= M; ++p) {
        if (!is_constrained[p]) {
            free_pots_count++;
        }
        Demand[p] = free_pots_count;
    }

    // Check Hall's condition on intervals.
    for (int k = 1; k <= M; ++k) {
        if (Prefix_RU[k] < Demand[k]) {
            return false;
        }
    }

    return true;
}

int main() {
    // Optimization for fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        if (solve()) {
            cout << "yes\n";
        } else {
            cout << "no\n";
        }
    }
    return 0;
}
