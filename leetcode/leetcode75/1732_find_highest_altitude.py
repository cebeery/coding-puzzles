"""
There is a biker going on a road trip.
The road trip consists of n + 1 points at different altitudes.
The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n
where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n).
Return the highest altitude of a point.

Constraints:
n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100
-----------
Results
Runtime: 0 ms - beats 100.00%
Memory: 17.70 MB - beats 51.22%
"""
import tester


def solution(gain: list[int]) -> int:
    peak = 0
    curr = 0
    for diff in gain:
        curr += diff
        if curr > peak:
            peak = curr
    return peak


tester.test([[-5,1,5,0,-7]], 1, solution)
tester.test([[-4,-3,-2,-1,4,3,2]], 0, solution)
