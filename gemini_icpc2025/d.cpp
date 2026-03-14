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
#include <string>
#include <algorithm>
#include <cstdint>
#include <cstring>

using namespace std;

// Global definitions for directions
const char DIRS[] = {'N', 'E', 'S', 'W'};
const int DR[] = {-1, 0, 1, 0};
const int DC[] = {0, 1, 0, -1};

// Helper to convert direction character to index (0-3)
int dir_to_idx(char d) {
    for (int i = 0; i < 4; ++i) {
        if (DIRS[i] == d) return i;
    }
    return -1; // Should not happen based on problem statement
}

void solve() {
    // Optimization for fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int R, C;
    if (!(cin >> R >> C)) return;

    vector<string> grid(R);
    int start_r = -1, start_c = -1;
    for(int i=0; i<R; ++i) {
        cin >> grid[i];
        for(int j=0; j<C; ++j) {
            if (grid[i][j] == 'S') {
                start_r = i;
                start_c = j;
            }
        }
    }
    string S;
    if (!(cin >> S)) return;

    // Lambda function to check if a cell is valid (within bounds and not rocky)
    auto is_valid = [&](int r, int c) {
        if (r < 0 || r >= R || c < 0 || c >= C) return false;
        return grid[r][c] != '#';
    };

    // Reachability matrix using bitmasks (4x4 bits) for transitive closure of constraints.
    // Reach[i] stores the bitmask of nodes reachable from i (meaning i < j). Bit j corresponds to node j.
    uint8_t Reach[4];

    auto reset_Reach = [&]() {
        memset(Reach, 0, sizeof(Reach));
    };

    // Helper to check if i reaches j (i < j).
    auto reaches = [&](int i, int j) {
        return (Reach[i] >> j) & 1;
    };

    // Helper to add an edge i -> j (i < j) and update transitive closure incrementally.
    // This is O(V) where V=4.
    auto add_edge_and_update_TC = [&](int U, int V) {
        if (reaches(U, V)) return;

        // 1. U reaches V and whatever V reaches.
        // Reach[U] |= (1 << V) | Reach[V];
        Reach[U] |= (1 << V);
        Reach[U] |= Reach[V];

        // 2. Update predecessors of U.
        for(int X=0; X<4; ++X) {
            if (reaches(X, U)) {
                // X reaches U. So X now reaches whatever U reaches.
                Reach[X] |= Reach[U];
            }
        }
    };

    reset_Reach();
    long long changes = 0;
    int cur_r = start_r;
    int cur_c = start_c;

    // Greedy approach: process moves and accumulate constraints until a conflict occurs.
    for (char move_char : S) {
        int move_idx = dir_to_idx(move_char);

        // 1. Determine valid moves V_i
        vector<int> V;
        for(int i=0; i<4; ++i) {
            int nr = cur_r + DR[i];
            int nc = cur_c + DC[i];
            if (is_valid(nr, nc)) {
                V.push_back(i);
            }
        }

        // 2. Determine constraints C_i. The actual move must precede other valid moves.
        vector<int> others;
        for(int d_idx : V) {
            if (d_idx != move_idx) {
                others.push_back(d_idx);
            }
        }

        // 3. Check for conflicts
        bool conflict = false;
        for(int D_idx : others) {
            // New constraint: move_idx < D_idx.
            // Conflict if D_idx < move_idx is already required (D_idx reaches move_idx).
            if (reaches(D_idx, move_idx)) {
                conflict = true;
                break;
            }
        }

        // 4. Handle conflict
        if (conflict) {
            changes++;
            reset_Reach();
        }

        // 5. Update Reachability with the new constraints
        for(int D_idx : others) {
            add_edge_and_update_TC(move_idx, D_idx);
        }

        // 6. Update position
        cur_r += DR[move_idx];
        cur_c += DC[move_idx];
    }

    cout << changes << "\n";
}

int main() {
    solve();
    return 0;
}
