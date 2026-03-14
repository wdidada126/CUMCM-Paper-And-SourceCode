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
#include <set>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdlib>

using namespace std;

// Global variables to store N and the current K
int N;
long long current_K;

// Function to perform a move and get the new K
long long rotate_wheel(int i, long long j) {
    if (j == 0) return current_K;
    
    cout << i << " " << j << endl;
    
    long long k;
    if (!(cin >> k)) {
        // Handle unexpected termination or error
        exit(0); 
    }
    current_K = k;
    
    if (k == 1) {
        exit(0); // We won!
    }
    return k;
}

// Phase 1: Reach K=N. O(N^2) moves.
void phase1() {
    set<int> unique_wheels;

    while (current_K < N) {
        bool k_increased = false;

        for (int i = 1; i <= N; ++i) {
            if (unique_wheels.count(i)) {
                continue;
            }

            long long start_K = current_K;
            bool found_increase = false;

            // Test wheel i by rotating it N-1 times by 1.
            for (int j = 1; j < N; ++j) {
                rotate_wheel(i, 1);
                
                if (current_K > start_K) {
                    found_increase = true;
                    break;
                }
            }

            if (found_increase) {
                k_increased = true;
                break; // Break the 'i' loop
            } else {
                // Wheel i is unique.
                unique_wheels.insert(i);
                
                // Revert wheel i. We rotated N-1 times. Rotate by 1 more to complete the cycle.
                rotate_wheel(i, 1);
                // current_K should be back to start_K.
            }
        }
        
        // If K < N, k_increased must be true. We rely on the mathematical guarantee.
    }
}

// Phase 2: Identify D_i's. O(N^2) moves.
vector<long long> phase2() {
    // We are at K=N.
    
    vector<long long> D(N + 1, 0);

    for (int i = 2; i <= N; ++i) {
        long long d_found = 0;
        
        // Test d=1 to N-1.
        for (int d = 1; d < N; ++d) {
            // Rotate i by -1, 1 by 1.
            rotate_wheel(i, -1);
            rotate_wheel(1, 1);
            
            if (current_K == N) {
                d_found = d;
                break;
            }
        }
        
        D[i] = d_found;
        
        // Revert rotations.
        
        // If d_found > 0, we performed d_found steps.
        // If d_found == 0, we performed N-1 steps. (Should not happen if K=N).
        
        long long total_rotation = d_found > 0 ? d_found : (N - 1);
        
        // We rotated i by -total_rotation, 1 by total_rotation.
        
        // Revert i by total_rotation.
        rotate_wheel(i, total_rotation);
        
        // Revert 1 by -total_rotation.
        rotate_wheel(1, -total_rotation);
        
        // After reverting, K should be back to N. 
    }
    return D;
}

// Phase 3: Align wheels. O(N) moves.
void phase3(const vector<long long>& D) {
    for (int i = 2; i <= N; ++i) {
        if (D[i] != 0) {
            // Rotate wheel i by -D[i] to align it with wheel 1.
            rotate_wheel(i, -D[i]);
        }
    }
}

void solve() {
    // We don't use ios_base::sync_with_stdio(false); cin.tie(NULL); because we need cout to flush before cin.
    
    // Read N
    if (!(cin >> N)) return;

    // Read initial K
    if (!(cin >> current_K)) return;

    if (current_K == 1) return;

    // Phase 1: Reach K=N.
    phase1();

    // Phase 2: Identify D_i's.
    vector<long long> D = phase2();

    // Phase 3: Align wheels.
    phase3(D);
    
    // We should have exited by now when K=1. 
}

int main() {
    solve();
    return 0;
}
