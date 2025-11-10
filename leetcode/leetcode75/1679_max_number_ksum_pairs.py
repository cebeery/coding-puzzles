"""
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k
and remove them from the array.

Return the maximum number of operations you can perform on the array.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
-----------
Results
Runtime: 494 ms - beats 83.35%
Memory: 30.73 MB - beats 16.85%

Looking at other solutions, sort does better even though
 O(n log n) should be worse than O(n)
"""
from collections import defaultdict
import tester

def solution(nums: list[int], k: int) -> int:
    unmatched = defaultdict(int)
    match_ct = 0
    for num in nums:
        pair = k - num
        if unmatched[pair] > 0:
            unmatched[pair] -= 1
            match_ct += 1
        else:
            unmatched[num] += 1

    return match_ct


tester.test([[1,2,3,4], 5], 2, solution)
tester.test([[3,1,3,4,3], 6], 1, solution)
