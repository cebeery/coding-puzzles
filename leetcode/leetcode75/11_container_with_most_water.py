"""
You are given an integer array height of length n.
There are n vertical lines drawn such that
the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
-----------
Results
Runtime: 65 ms - beats 92.38%
Memory: 28.56 MB - beats 23.86%
"""
import tester


def solution(height: list[int]) -> int:
    l,r = 0, len(height)-1
    max_volume = 0

    while l<r:
        if height[l] < height[r]:
            curr = height[l] * (r - l)
            l += 1
        else:
            curr = height[r] * (r - l)
            r -= 1
        max_volume = max(max_volume, curr)

    return max_volume

tester.test([[1,8,6,2,5,4,8,3,7]], 49, solution)
tester.test([[1,1]], 1, solution)
