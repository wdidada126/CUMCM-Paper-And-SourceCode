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
#include <iomanip>
#include <cstring>

using namespace std;

// Global variables to store the problem input and DP state.
int S, R, D;

struct Output {
    int to;
    double p;
};

// Graph representation
vector<vector<int>> station_ducts;
vector<vector<Output>> duct_outputs;

// DP array for M(i, C).
vector<double> M_node;

// Function to calculate G(C) = M(1, C) using DP.
double calculate_G(const vector<double>& C) {
    // Initialize for reservoirs. S+1 to S+R.
    // C is 0-indexed, reservoirs are S+1-indexed.
    for (int k = 0; k < R; ++k) {
        M_node[S + 1 + k] = C[k];
    }

    // Process stations in reverse order (from S down to 1).
    for (int i = S; i >= 1; --i) {
        double max_val = 0;
        for (int d : station_ducts[i]) {
            double val_d = 0;
            for (const auto& out : duct_outputs[d]) {
                // out.to is guaranteed to be > i.
                val_d += out.p * M_node[out.to];
            }
            if (val_d > max_val) {
                max_val = val_d;
            }
        }
        M_node[i] = max_val;
    }
    return M_node[1];
}

// Optimization for R=1
double solve_R1() {
    return calculate_G({1.0});
}

// Optimization for R=2 using Ternary Search
double solve_R2() {
    double L = 0, R = 1;
    // Use 70 iterations for high precision. (2/3)^70 approx 10^-12.
    for(int i=0; i<70; ++i) {
        double m1 = L + (R-L)/3;
        double m2 = R - (R-L)/3;
        // C = (t, 1-t)
        double v1 = calculate_G({m1, 1-m1});
        double v2 = calculate_G({m2, 1-m2});
        if (v1 < v2) {
            R = m2;
        } else {
            L = m1;
        }
    }
    return calculate_G({(L+R)/2, 1-(L+R)/2});
}

// Optimization for R=3 using Nested Ternary Search
// Number of iterations for R=3. 60 iterations gives precision around 10^-10.
const int NUM_ITER = 60;

// Inner ternary search for t2, given t1. Minimizes G(t1, t2, 1-t1-t2).
double H(double t1) {
    // Clamp t1 to [0, 1] just in case of precision issues
    if (t1 < 0) t1 = 0;
    if (t1 > 1) t1 = 1;
    
    double L = 0, R = 1 - t1;
    
    // If the interval is very small, just evaluate.
    // We must ensure the weights sum to 1 and are non-negative.
    if (R < 1e-12) {
        return calculate_G({t1, 0.0, 1.0-t1});
    }

    for(int i=0; i<NUM_ITER; ++i) {
        double m1 = L + (R-L)/3;
        double m2 = R - (R-L)/3;
        
        double c3_1 = 1.0 - t1 - m1;
        double c3_2 = 1.0 - t1 - m2;

        // Handle potential precision issues leading to slightly negative c3.
        if (c3_1 < 0) c3_1 = 0;
        if (c3_2 < 0) c3_2 = 0;

        double v1 = calculate_G({t1, m1, c3_1});
        double v2 = calculate_G({t1, m2, c3_2});
        
        if (v1 < v2) {
            R = m2;
        } else {
            L = m1;
        }
    }
    double t2 = (L+R)/2;
    double c3 = 1.0-t1-t2;
    if (c3 < 0) c3 = 0;
    return calculate_G({t1, t2, c3});
}

double solve_R3() {
    double L = 0, R = 1;
    for(int i=0; i<NUM_ITER; ++i) {
        double m1 = L + (R-L)/3;
        double m2 = R - (R-L)/3;
        double v1 = H(m1);
        double v2 = H(m2);
        if (v1 < v2) {
            R = m2;
        } else {
            L = m1;
        }
    }
    return H((L+R)/2);
}

void solve() {
    // Set up input reading for faster I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> S >> R >> D)) return;

    // Initialize data structures. Nodes are 1-indexed.
    // Stations 1..S. Reservoirs S+1..S+R. Ducts 1..D.
    station_ducts.resize(S + 1);
    duct_outputs.resize(D + 1);
    M_node.resize(S + R + 1);

    for (int d = 1; d <= D; ++d) {
        int i, n;
        // Reading input robustly, although typically unnecessary in contests.
        if (!(cin >> i >> n)) return;
        station_ducts[i].push_back(d);
        for (int j = 0; j < n; ++j) {
            int o, p;
            if (!(cin >> o >> p)) return;
            duct_outputs[d].push_back({o, p / 100.0});
        }
    }

    double result;
    if (R == 1) {
        result = solve_R1();
    } else if (R == 2) {
        result = solve_R2();
    } else if (R == 3) {
        result = solve_R3();
    } else {
        result = 0; // Should not happen
    }

    // Output the result as a percentage.
    cout << fixed << setprecision(12) << result * 100.0 << "\n";
}

int main() {
    solve();
    return 0;
}
