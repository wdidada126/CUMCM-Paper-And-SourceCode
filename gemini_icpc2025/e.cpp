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
#include <numeric>
#include <algorithm>
#include <unordered_map>
#include <chrono>
#include <cstdint>
#include <utility>

using namespace std;

// The solution utilizes the Role Graph model combined with the Principle of Inclusion-Exclusion (PIE).
// We construct a graph with 2N nodes representing Home (H_i) and Destination (D_i) roles for each city i.
// A courier (A, B) adds an edge (H_A, D_B).
// Connected components in the Role Graph (K) define cliques of connected cities V(K).
// The total number of connected pairs is the number of edges in the union of these cliques.
// Since a city has only two roles (H and D), triple intersections of V(K) for distinct K are empty.
// PIE simplifies to T1 - T2.
// T1 (E_C) is the sum of pairs in each clique. T2 (E_O) is the sum of pairs in the overlaps between cliques.
// We maintain T1 and T2 dynamically using DSU and a Component Graph that tracks overlaps.

// Custom hash function for robustness and efficiency of std::unordered_map.
// This helps avoid worst-case scenarios with hash collisions.
struct custom_hash {
    // Uses splitmix64 for fast, high-quality hashing.
    static uint64_t splitmix64(uint64_t x) {
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }
    // Uses a fixed random seed initialized at runtime.
    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

using HashMap = std::unordered_map<int, int, custom_hash>;

const int MAXN = 200005;
const int MAX_NODES = 2 * MAXN; 

int N, M;
// DSU Parent array.
int Parent[MAX_NODES + 1];
// clique_size[R] stores |V(R)|. It is <= N, so int is sufficient.
int clique_size[MAX_NODES + 1];
// overlaps[R] stores the Component Graph adjacency list (weights are overlap sizes).
vector<HashMap> overlaps;

long long E_C = 0; // T1
long long E_O = 0; // T2

// Helper function for nC2 (n choose 2).
inline long long binom2(long long n) {
    if (n < 2) return 0;
    return n * (n - 1) / 2;
}

// DSU Find with path compression.
int Find(int i) {
    if (Parent[i] == i) return i;
    return Parent[i] = Find(Parent[i]);
}

// DSU Union operation.
void Union(int A, int B) {
    int R_A = Find(A);
    int R_B = Find(B);

    if (R_A == R_B) return;

    // Small-to-large heuristic on the size of the overlaps map (Component Graph degree).
    // Ensures O(N log N) total expected time for merges.
    if (overlaps[R_A].size() > overlaps[R_B].size()) {
        swap(R_A, R_B);
    }
    // R_A is smaller, merged into R_B.

    // 1. Calculate k_AB (overlap between A and B)
    int k_AB = 0;
    auto it_AB = overlaps[R_A].find(R_B);
    if (it_AB != overlaps[R_A].end()) {
        k_AB = it_AB->second;
    }

    // 2. Update E_O for the edge (A, B) which is internalized.
    E_O -= binom2(k_AB);

    // 3. Remove mutual connection from maps
    if (k_AB > 0) {
        // Erase from R_A using the iterator.
        overlaps[R_A].erase(it_AB);
        overlaps[R_B].erase(R_A);
    }

    // 4. Update Clique sizes and E_C
    long long V_A = clique_size[R_A];
    long long V_B = clique_size[R_B];
    // |V_new| = |V_A| + |V_B| - k_AB
    long long V_new = V_A + V_B - k_AB;

    E_C -= binom2(V_A);
    E_C -= binom2(V_B);
    E_C += binom2(V_new);

    clique_size[R_B] = (int)V_new;

    // Optimization: Reserve space to potentially avoid rehashes during merge.
    overlaps[R_B].reserve(overlaps[R_B].size() + overlaps[R_A].size());

    // 5. Merge overlap maps. Iterate over R_A's neighbors (R_C).
    for (const auto& pair_AC : overlaps[R_A]) {
        int R_C = pair_AC.first;
        int k_AC = pair_AC.second;

        // Use operator[] to efficiently access/insert into R_B's map.
        // If R_C is not present, it inserts it with value 0.
        int& k_BC_ref = overlaps[R_B][R_C]; 
        int k_BC = k_BC_ref; 

        // Update E_O. Delta = k_AC * k_BC. (Since triple intersections are empty).
        // Must use long long multiplication to prevent overflow (N*N can exceed 2^32).
        E_O += (long long)k_AC * k_BC;

        // Update O[B]. W_new = W_AC + W_BC.
        k_BC_ref += k_AC;
        int k_new = k_BC_ref;
        
        // Update O[C]. R_A is replaced by R_B. Maintain invariant that keys are representatives.
        overlaps[R_C].erase(R_A);
        overlaps[R_C][R_B] = k_new;
    }

    // 6. Update DSU structure
    Parent[R_A] = R_B;
    // overlaps[R_A].clear(); // Optional: memory cleanup, potentially useful for performance too.
}

void Solve() {
    // Set up I/O optimization
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N >> M)) return;

    int num_nodes = 2 * N;
    // Initialize data structures
    overlaps.resize(num_nodes + 1);

    // Initialize DSU sets and clique sizes.
    // Nodes 1..N are H_i. Nodes N+1..2N are D_i.
    for (int i = 1; i <= num_nodes; ++i) {
        Parent[i] = i;
        clique_size[i] = 1;
    }

    // Initialize overlaps (bridges). City i bridges H_i (i) and D_i (N+i).
    for (int i = 1; i <= N; ++i) {
        int H = i;
        int D = N + i;
        // Optimization: reserve initial capacity.
        overlaps[H].reserve(1);
        overlaps[D].reserve(1);
        overlaps[H][D] = 1;
        overlaps[D][H] = 1;
    }

    // Process couriers
    for (int i = 0; i < M; ++i) {
        int A, B;
        if (!(cin >> A >> B)) break;

        // Courier connects H_A (node A) and D_B (node N+B).
        Union(A, N + B);

        // Result is E_C - E_O.
        cout << (E_C - E_O) << "\n";
    }
}

int main() {
    Solve();
    return 0;
}
