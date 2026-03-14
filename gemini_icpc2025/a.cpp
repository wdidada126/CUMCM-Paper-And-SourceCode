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
#include <numeric>
#include <cmath>
#include <cstring>

using namespace std;

// Global variable for N.
int N;
struct Node {
    int L=0, R=0, P=0;
};
// We will use 1-based indexing. tree[0] is unused.
vector<Node> initial_tree;

// Function to find candidates.
// A node x is a candidate if it could have been the last element inserted, 
// resulting in a valid skew heap before the insertion.
vector<int> find_candidates(const vector<Node>& tree, int root) {
    if (root == 0) return {};

    // 1. Find vk, the highest node on the left spine without a right child.
    int vk = 0;
    int curr = root;
    while(curr != 0) {
        if (tree[curr].R == 0) {
            vk = curr;
            break;
        }
        curr = tree[curr].L;
    }

    // If all nodes on the left spine have a right child, no candidate exists.
    // This implies the tree structure is invalid for a skew heap constructed by sequential insertions.
    if (vk == 0) return {};

    vector<int> candidates;
    // vk is always a valid candidate.
    candidates.push_back(vk);

    // 2. Check v_{k+1} (the left child of vk).
    int vk_plus_1 = tree[vk].L;
    if (vk_plus_1 != 0) {
        // It is a candidate IFF it is a leaf (L=0 and R=0).
        // This is derived from conditions C2 (R=0) and C3 (L=0 because R(vk)=0).
        if (tree[vk_plus_1].L == 0 && tree[vk_plus_1].R == 0) {
            candidates.push_back(vk_plus_1);
        }
    }
    return candidates;
}

// Function to perform reversal. Needs to modify the tree structure.
int reverse_insertion(vector<Node>& tree, int x, int root) {
    int w = tree[x].L;
    int px = tree[x].P;

    // 1. Remove x, promote w (left child of x).
    if (px == 0) {
        // x is the root.
        root = w;
        if (w != 0) tree[w].P = 0;
    } else {
        // x must be the left child of px (as it's on the left spine).
        tree[px].L = w;
        if (w != 0) tree[w].P = px;
    }
    
    // Clear x's connections, although not strictly necessary as x won't be reused.
    tree[x].L = tree[x].R = tree[x].P = 0;

    // 2. Swap children along the path from px upwards to the root.
    // This reverses the swaps that occurred during the insertion of x.
    int curr = px;
    while (curr != 0) {
        swap(tree[curr].L, tree[curr].R);
        curr = tree[curr].P;
    }
    return root;
}

// Helper function to run the greedy strategy.
// strategy = 0 for minimal P (max removal), 1 for maximal P (min removal).
vector<int> find_permutation(int strategy) {
    // Work on a copy of the tree structure.
    vector<Node> tree = initial_tree;
    // The root is always 1 initially if N>0, as it's the smallest element.
    int root = (N > 0) ? 1 : 0;
    vector<int> reversed_P;
    
    for (int i = 0; i < N; ++i) {
        vector<int> candidates = find_candidates(tree, root);
        
        if (candidates.empty()) {
            return {}; // Impossible
        }
        
        int x;
        if (strategy == 0) {
            // Maximize removal (for lexicographically minimal P)
            x = candidates[0];
            for (int c : candidates) {
                if (c > x) x = c;
            }
        } else {
            // Minimize removal (for lexicographically maximal P)
            x = candidates[0];
            for (int c : candidates) {
                if (c < x) x = c;
            }
        }
        
        reversed_P.push_back(x);
        root = reverse_insertion(tree, x, root);
    }
    
    reverse(reversed_P.begin(), reversed_P.end());
    return reversed_P;
}


void solve() {
    // Set up I/O optimization
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N)) return;

    initial_tree.resize(N + 1);
    for (int i = 1; i <= N; ++i) {
        int l, r;
        if (!(cin >> l >> r)) return; // Handle read error
        initial_tree[i].L = l;
        initial_tree[i].R = r;
        if (l != 0) initial_tree[l].P = i;
        if (r != 0) initial_tree[r].P = i;
    }

    // Strategy 0: Minimal P
    vector<int> min_P = find_permutation(0);
    if (min_P.empty()) {
        cout << "impossible\n";
        return;
    }
    
    // Strategy 1: Maximal P
    vector<int> max_P = find_permutation(1);
    // max_P should also be valid if min_P is valid.
    
    // Output results
    for (int i = 0; i < N; ++i) {
        cout << min_P[i] << (i == N - 1 ? "" : " ");
    }
    cout << "\n";
    
    for (int i = 0; i < N; ++i) {
        cout << max_P[i] << (i == N - 1 ? "" : " ");
    }
    cout << "\n";
}

int main() {
    solve();
    return 0;
}
