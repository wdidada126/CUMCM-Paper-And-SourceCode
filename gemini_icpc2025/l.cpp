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
#include <algorithm>

using namespace std;

// Define a structure to represent a closed interval [start, end].
struct Interval {
    long long start, end;
    // Sort by start point.
    bool operator<(const Interval& other) const {
        if (start != other.start) return start < other.start;
        return end < other.end;
    }
};

void solve() {
    // Set up I/O for faster performance
    ios_base::sync_with_stdio(false);
    // cin.tie(NULL); // Usually safe, but sometimes flushing is needed in interactive problems or when mixing C/C++ I/O. Here it should be fine.

    int N;
    long long Xc, Yc, Xa, Ya;
    
    // Read Input N and coordinates of C and A.
    if (!(cin >> N >> Xc >> Yc >> Xa >> Ya)) return;

    // If the movement is northward or purely horizontal, the cost is 0.
    if (Yc <= Ya) {
        cout << fixed << setprecision(8) << 0.0 << "\n";
        return;
    }

    // We are moving southward.
    long long Y_start = Ya;
    long long Y_end = Yc;
    long long total_dist = Y_end - Y_start;

    // Read the rectangles and store their y-intervals.
    vector<Interval> intervals;
    for (int i = 0; i < N; ++i) {
        long long x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        // y1 is the bottom coordinate (SW), y2 is the top coordinate (NE).
        intervals.push_back({y1, y2});
    }

    // Sort the intervals by start coordinate. O(N log N).
    sort(intervals.begin(), intervals.end());

    // Merge overlapping intervals. This identifies connected components where we can move freely vertically by switching between rectangles horizontally. O(N).
    vector<Interval> merged;
    if (intervals.empty()) {
        // No shades.
    } else {
        Interval current = intervals[0];
        for (int i = 1; i < N; ++i) {
            // Check for overlap or touch (assuming closed intervals).
            // Since horizontal movement is free, if y-ranges overlap or touch, we can switch between them.
            if (intervals[i].start <= current.end) {
                // Merge.
                current.end = max(current.end, intervals[i].end);
            } else {
                // No overlap, finalize the current merged interval.
                merged.push_back(current);
                current = intervals[i];
            }
        }
        merged.push_back(current);
    }

    // Calculate the total shaded length within the target range [Ya, Yc]. O(N).
    long long shaded_dist = 0;
    for (const auto& interval : merged) {
        // Intersection of [interval.start, interval.end] and [Y_start, Y_end].
        long long start = max(interval.start, Y_start);
        long long end = min(interval.end, Y_end);
        
        // Length of intersection.
        if (end > start) {
            shaded_dist += (end - start);
        }
    }

    // The minimum cost is the total vertical distance minus the shaded vertical distance.
    long long cost = total_dist - shaded_dist;
    
    // Output the result with required precision.
    cout << fixed << setprecision(8) << (double)cost << "\n";
}

int main() {
    solve();
    return 0;
}
