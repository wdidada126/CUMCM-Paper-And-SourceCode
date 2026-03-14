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
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <map>

using namespace std;

typedef long long ll;

const ll INF = 2e18;
const ll DP_IMPOSSIBLE = -2;

ll M;
int N;
vector<ll> P;
ll P_min;
vector<ll> S_r;
vector<bool> R_set;
ll S_max = 0;

ll RequiredSigns[9] = {0};

void update_required_signs(ll X) {
    if (X == 0) {
        RequiredSigns[0] = max(RequiredSigns[0], 1LL);
        return;
    }
    string s = to_string(X);
    ll counts[10] = {0};
    for(char c : s) {
        counts[c-'0']++;
    }
    
    for(int i=0; i<=8; ++i) {
        if (i != 6) {
            RequiredSigns[i] = max(RequiredSigns[i], counts[i]);
        }
    }
    // For 6/9 signs.
    RequiredSigns[6] = max(RequiredSigns[6], counts[6] + counts[9]);
}

// Global variables for DP
ll P_min_DP;
const vector<bool>* R_set_DP_ptr;
vector<int> L_digits, R_digits;
int D_DP;
int target_digit; // -1 for 6/9 combo.

// Memoization table. pos, rem, tL, tH.
// D <= 18 (for M-1). M can be 10^18 (19 digits), but we handle M separately.
ll Memo[19][1001][2][2];

ll dp_solve(int pos, int rem, bool tL, bool tH) {
    if (pos == D_DP) {
        return (*R_set_DP_ptr)[rem] ? 0 : DP_IMPOSSIBLE;
    }
    if (Memo[pos][rem][tL][tH] != -1) {
        return Memo[pos][rem][tL][tH];
    }

    ll max_count = DP_IMPOSSIBLE;
    int D_min = tL ? L_digits[pos] : 0;
    int D_max = tH ? R_digits[pos] : 9;

    for (int digit = D_min; digit <= D_max; ++digit) {
        bool new_tL = tL && (digit == D_min);
        bool new_tH = tH && (digit == D_max);
        int new_rem = (rem * 10LL + digit) % P_min_DP;

        ll count = dp_solve(pos+1, new_rem, new_tL, new_tH);
        
        if (count != DP_IMPOSSIBLE) {
            ll cost = 0;
            if (target_digit != -1) {
                if (digit == target_digit) cost = 1;
            } else {
                // 6/9 combo
                if (digit == 6 || digit == 9) cost = 1;
            }
            max_count = max(max_count, cost + count);
        }
    }
    return Memo[pos][rem][tL][tH] = max_count;
}

ll calculate_max_count(ll L, ll R, ll P_min, const vector<bool>& R_set, int target) {
    if (L > R) return 0;

    P_min_DP = P_min;
    R_set_DP_ptr = &R_set;
    target_digit = target;

    string SL = to_string(L);
    string SR = to_string(R);
    int DL = SL.length();
    int DR = SR.length();

    ll max_c = 0;

    for (int len = DL; len <= DR; ++len) {
        // Determine L_bound and R_bound for length len.
        
        L_digits.clear();
        R_digits.clear();

        // For L_bound.
        if (len == DL) {
            for(char c: SL) L_digits.push_back(c-'0');
        } else {
            // Smallest number of length len. 10...0.
            L_digits.assign(len, 0);
            L_digits[0] = 1;
        }

        // For R_bound.
        if (len == DR) {
            for(char c: SR) R_digits.push_back(c-'0');
        } else {
            // Largest number of length len. 99...9.
            R_digits.assign(len, 9);
        }

        D_DP = len;
        
        // Initialize Memo table
        // We only need to initialize up to D_DP and P_min_DP, but initializing all is fine too.
        memset(Memo, -1, sizeof(Memo));

        ll count = dp_solve(0, 0, true, true);
        if (count != DP_IMPOSSIBLE) {
            max_c = max(max_c, count);
        }
    }
    return max_c;
}


void solve() {
    // Set up input
    if (!(cin >> M >> N)) return;
    P.resize(N);
    for (int i = 0; i < N; ++i) {
        cin >> P[i];
    }

    if (N == 0) {
        // If N=0, only score 0 is reachable. If M>=0, 0 is reachable.
        update_required_signs(0);
    } else {
        // 1. Calculate P_min.
        P_min = P[0];
        for(ll p : P) P_min = min(P_min, p);

        // 2. Calculate S_r using Dijkstra's.
        S_r.assign(P_min, INF);
        // {distance, remainder}
        priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> pq;

        S_r[0] = 0;
        pq.push({0, 0});

        while(!pq.empty()) {
            ll d = pq.top().first;
            int r = pq.top().second;
            pq.pop();

            if(d > S_r[r]) continue;

            for(ll p : P) {
                int next_r = (r + p) % P_min;
                ll next_d = d + p;
                if(next_d < S_r[next_r]) {
                    S_r[next_r] = next_d;
                    pq.push({next_d, next_r});
                }
            }
        }

        // 3. Calculate R_set and S_max.
        R_set.assign(P_min, false);
        S_max = 0;
        for(int r=0; r<P_min; ++r) {
            if(S_r[r] != INF) {
                R_set[r] = true;
                S_max = max(S_max, S_r[r]);
            }
        }

        // 5. Handle M. M is always reachable if M>=1 and N>=1.
        if (M >= 1) {
            update_required_signs(M);
        } else if (M==0) {
            update_required_signs(0);
        }

        // 6. Handle scores up to min(M-1, S_max).
        if (M >= 1) {
            ll limit = min(M-1, S_max);

            for(int r=0; r<P_min; ++r) {
                if(S_r[r] != INF && S_r[r] <= limit) {
                    ll X = S_r[r];
                    // Handle X=0 only once, for r=0.
                    if (r != 0 || S_r[r] != 0 || (r==0 && S_r[r]==0)) {
                         update_required_signs(X);
                    }
                   
                    // Arithmetic progression: S_r[r] + k * P_min
                    // Check for overflow before addition, although unlikely given S_max approx 10^6.
                    while (limit - X >= P_min) {
                        X += P_min;
                        update_required_signs(X);
                    }
                }
            }
            // Special handling for 0 if not covered. It should be covered by r=0, S_0=0.
        }

        // 7. Handle scores in (S_max, M-1].
        if (M > 1 && M-1 > S_max) {
            ll L = S_max + 1;
            ll R = M - 1;

            // Digits 0-5, 7-8.
            for (int d=0; d<=8; ++d) {
                if (d == 6) continue;
                ll count = calculate_max_count(L, R, P_min, R_set, d);
                RequiredSigns[d] = max(RequiredSigns[d], count);
            }
            
            // For 6/9 combo. Target is -1.
            ll count69 = calculate_max_count(L, R, P_min, R_set, -1);
            RequiredSigns[6] = max(RequiredSigns[6], count69);
        }
    }

    // Output results
    for (int i = 0; i <= 8; ++i) {
        if (RequiredSigns[i] > 0) {
            cout << i << " " << RequiredSigns[i] << "\n";
        }
    }
}

int main() {
    // Optimize input/output operations
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
    return 0;
}
