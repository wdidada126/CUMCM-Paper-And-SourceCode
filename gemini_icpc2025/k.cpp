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
#include <queue>
#include <algorithm>
#include <climits>
#include <cmath>

using namespace std;

typedef long long ll;

int N, M, K;
int TX, TY;

// Adjacency lists for the bipartite graph.
// adjX[x] stores pairs of (y, d)
vector<vector<pair<int, ll>>> adjX, adjY;
// Potentials
vector<ll> deltaX, deltaY;
// Component IDs (0 means not visited/isolated)
vector<int> compX, compY;
// Minimum potentials for each component
vector<ll> minX_C, minY_C;

// Function to process a connected component using BFS
bool process_component(int start_x, int C) {
    // Initialize minimum potentials for the current component
    ll mX = LLONG_MAX, mY = LLONG_MAX;
    queue<pair<int, int>> q; // type (0 for X, 1 for Y), index

    // Start BFS from start_x
    compX[start_x] = C;
    deltaX[start_x] = 0;
    mX = 0;
    q.push({0, start_x});

    while (!q.empty()) {
        auto [type, u] = q.front();
        q.pop();

        if (type == 0) { // X node
            for (auto& edge : adjX[u]) {
                int v = edge.first;
                ll d = edge.second;
                if (compY[v] == 0) {
                    compY[v] = C;
                    deltaY[v] = d - deltaX[u];
                    if (mY == LLONG_MAX || deltaY[v] < mY) {
                        mY = deltaY[v];
                    }
                    q.push({1, v});
                } else if (compY[v] == C) {
                    // Check consistency
                    if (deltaX[u] + deltaY[v] != d) return false;
                }
            }
        } else { // Y node
            for (auto& edge : adjY[u]) {
                int v = edge.first;
                ll d = edge.second;
                if (compX[v] == 0) {
                    compX[v] = C;
                    deltaX[v] = d - deltaY[u];
                    if (mX == LLONG_MAX || deltaX[v] < mX) {
                        mX = deltaX[v];
                    }
                    q.push({0, v});
                } else if (compX[v] == C) {
                    // Check consistency
                    if (deltaX[v] + deltaY[u] != d) return false;
                }
            }
        }
    }

    // Check internal non-negativity
    // A component derived from constraints must have at least one X and one Y node.
    // If either mX or mY is LLONG_MAX, it means the component was trivial (e.g. isolated node), 
    // but we only start BFS if the node has edges.
    
    // If start_x had edges, it must have connected to some Y node, so mY should be updated.
    // If the graph is built correctly (bidirectionally), this should be fine.

    if (mX == LLONG_MAX) mX = 0; // Should be updated if any X node is reached
    if (mY == LLONG_MAX) mY = 0; // Should be updated if any Y node is reached

    if (mX + mY < 0) return false;

    // Store component statistics. Component ID C corresponds to index C-1.
    minX_C.push_back(mX);
    minY_C.push_back(mY);
    return true;
}

void solve() {
    // Set up input reading for faster I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N >> M >> K >> TX >> TY)) return;

    adjX.resize(N + 1);
    adjY.resize(M + 1);
    deltaX.resize(N + 1);
    deltaY.resize(M + 1);
    compX.resize(N + 1, 0);
    compY.resize(M + 1, 0);

    for (int i = 0; i < K; ++i) {
        int x, y;
        ll d;
        cin >> x >> y >> d;
        adjX[x].push_back({y, d});
        adjY[y].push_back({x, d});
    }

    int C = 0;
    // Iterate over all X nodes to find connected components
    for (int x = 1; x <= N; ++x) {
        // Start BFS if x is not visited and has constraints
        if (compX[x] == 0 && !adjX[x].empty()) {
            C++;
            if (!process_component(x, C)) {
                cout << "impossible" << endl;
                return;
            }
        }
    }
    
    // Also check Y nodes just in case there's a component consisting only of Y nodes connected to X nodes that we already processed? No, that's not possible.
    // However, we might have missed components if we only iterate through X nodes, IF there was a possibility of a component only having Y nodes. But that's not possible in a bipartite graph with edges.
    // But what if an X node has no edges, but a Y node has edges connecting to it?
    // If Y has an edge to X, then X also has an edge to Y (we build it bidirectionally).
    // So the iteration over X nodes that have edges is sufficient to discover all Type 1 components.

    // Calculate the minimum depth at (TX, TY).
    ll result;
    int c_tx = compX[TX];
    int c_ty = compY[TY];

    // A node is isolated if its component ID is 0. 
    // Note that even if a node has no edges, we consider it isolated in the context of constraints.
    // If a node has edges, it must have been assigned a component ID during the process phase.
    
    // Let's verify the definition of isolated. If adjX[x] is empty, it is isolated.
    // If compX[x] is 0, it means either it has no edges, or it has edges but we haven't processed it.
    // Since we iterated through all x, if compX[x] is 0, it must be that adjX[x] was empty.
    
    bool isolated_tx = (c_tx == 0);
    bool isolated_ty = (c_ty == 0);

    if (!isolated_tx && !isolated_ty) {
        // Case I: Both in components (Type 1).
        if (c_tx == c_ty) {
            // Case I.a: Same component.
            result = deltaX[TX] + deltaY[TY];
        } else {
            // Case I.b: Different components.
            // Component IDs are 1-indexed. Vector indices are 0-indexed.
            ll mXi = minX_C[c_tx-1];
            ll mYj = minY_C[c_ty-1];
            // Minimized V_i - V_j is -(mX(i) + mY(j)).
            // Result = -(mX(i) + mY(j)) + delta_tx + delta_ty.
            result = -(mXi + mYj) + deltaX[TX] + deltaY[TY];
        }
    } else if (isolated_tx && !isolated_ty) {
        // Case II: tx isolated, ty in C_j.
        int j = c_ty;
        ll mYj = minY_C[j-1];
        // Result: -m'_Y(j) + delta'_{ty}.
        result = -mYj + deltaY[TY];
    } else if (!isolated_tx && isolated_ty) {
        // Case III: tx in C_i, ty isolated.
        int i = c_tx;
        ll mXi = minX_C[i-1];
        // Result: -m_X(i) + delta_{tx}.
        result = -mXi + deltaX[TX];
    } else {
        // Case IV: Both isolated.
        result = 0;
    }

    cout << result << endl;
}

int main() {
    solve();
    return 0;
}
