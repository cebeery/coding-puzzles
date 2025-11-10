"""
Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
-----------
Results
Runtime: 72 ms - beats 81.96%
Memory: 20.33 MB - beats 52.11%
"""
import tester


def solution(nums: list[int], k: int) -> int:
    max_ones = 0
    curr = 0
    flips = 0
    l = r = 0

    while r < len(nums):
        # Not a one and no flips remain
        if not nums[r] and not k > flips:
            # Shrink left (until at least one zero removed to allow flipping)
            if not nums[l]:
                flips -= 1
            curr -= 1
            l += 1
            continue

        # increment counts and shift right forward
        if not nums[r]:
            flips += 1

        curr += 1
        if curr > max_ones:
            max_ones = curr
        r += 1

    return max_ones

tester.test([[1,1,1,0,0,0,1,1,1,1,0], 2], 6, solution)
tester.test([[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3], 10, solution)
