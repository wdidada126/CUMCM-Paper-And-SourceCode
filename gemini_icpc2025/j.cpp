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
#include <cmath>
#include <numeric>

using namespace std;

typedef long long ll;

// Function to check if T is achievable as a subset sum of the first K odd numbers.
// {1, 3, ..., 2K-1}. The sum is K^2. 
// Known property: The only gaps in [0, K^2] are 2 and K^2-2 (for K>=2).
bool IsAchievable(int K, ll T) {
    if (K < 0 || T < 0) return false;
    // Calculate K^2 using long long to prevent overflow.
    ll K2 = (ll)K * K;
    if (T > K2) return false;
    if (K == 0) return T == 0;
    
    // T=2 is never achievable as a sum of distinct positive odds.
    if (T == 2) return false;

    // Check for the gap K^2-2.
    if (K >= 2) {
        if (T == K2 - 2) return false;
    }
    return true;
}

// Modified Greedy Algorithm for Subset Sum of Odds (SSO).
// Finds a subset of indices {1..K} whose heights sum to T.
// Assumes T is achievable. Returns indices in decreasing order. O(K).
// This greedy approach works because if T is achievable by K elements, and T-L_K is achievable by K-1 elements, we can safely include K.
vector<int> SSO_indices(int K, ll T) {
    vector<int> S;
    for (int i = K; i >= 1; --i) {
        // Height of cup i.
        ll L = 2LL * i - 1;
        if (T >= L) {
            // Check if the remainder T-L is achievable by the remaining i-1 elements.
            if (IsAchievable(i - 1, T - L)) {
                S.push_back(i);
                T -= L;
            }
        }
    }
    // T should be 0 now.
    return S;
}

void solve() {
    // Set up I/O optimization
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    ll H;
    // Read Input
    if (!(cin >> N >> H)) return;

    // Use ll for N in calculations involving H or potential N^2 terms.
    ll N_ll = (ll)N;
    ll min_H = 2 * N_ll - 1;
    ll max_H = N_ll * N_ll;

    // 1. Check overall bounds.
    if (H < min_H || H > max_H) {
        cout << "impossible\n";
        return;
    }

    // 2. Check the known impossible gap H=N^2-2 (for N>=3).
    if (N >= 3 && H == max_H - 2) {
        cout << "impossible\n";
        return;
    }

    // 3. Handle the special case H=2N+1.
    // The standard Unimodal construction (Strategy U) fails because H' = 2, which is a gap.
    if (H == 2 * N_ll + 1) {
        // For N=3, H=7 (N^2-2), already handled.
        // This case applies for N>=4.
        if (N >= 4) {
            // Specific construction derived from Strategy F (N first):
            // Indices: N, 2, N-1, N-2, ..., 3, 1.
            vector<ll> heights;
            heights.reserve(N);
            heights.push_back(2 * N_ll - 1); // N
            heights.push_back(3);            // 2
            
            // N-1 down to 3.
            for (int i = N - 1; i >= 3; --i) {
                heights.push_back(2LL * i - 1);
            }
            heights.push_back(1);            // 1
            
            for (int i = 0; i < N; ++i) {
                cout << heights[i] << (i == N - 1 ? "" : " ");
            }
            cout << "\n";
            return;
        }
    }

    // 4. General case: Unimodal construction with peak N (Strategy U).
    // P = (P_L increasing, N, P_R decreasing). H = Sum(P_L) + (2N-1).
    // This works for all remaining achievable heights because the required subset sum Hp is not a gap.
    ll Hp = H - min_H;
    int K = N - 1;
    
    // Find the subset of indices S' (P_L) whose heights sum to Hp.
    vector<int> S_indices = SSO_indices(K, Hp);
    
    // Construct the permutation of indices.
    vector<int> P_indices;
    P_indices.reserve(N);
    
    // Track usage to find the complement (P_R).
    vector<bool> in_S(N + 1, false);
    for (int idx : S_indices) {
        in_S[idx] = true;
    }
    
    // Ascending part (P_L). SSO_indices returns them in decreasing order.
    // Iterate backwards to get increasing order.
    for (int i = S_indices.size() - 1; i >= 0; --i) {
        P_indices.push_back(S_indices[i]);
    }
    
    // Peak N.
    P_indices.push_back(N);
    
    // Descending part (P_R).
    for (int i = K; i >= 1; --i) {
        if (!in_S[i]) {
            P_indices.push_back(i);
        }
    }
    
    // Output the heights (2*index - 1).
    for (int i = 0; i < N; ++i) {
        // Use 2LL to ensure multiplication is done in long long.
        cout << (2LL * P_indices[i] - 1) << (i == N - 1 ? "" : " ");
    }
    cout << "\n";
}

int main() {
    solve();
    return 0;
}
