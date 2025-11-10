"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.
Return 0 if there is no such subarray.

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
-----------
Results
Runtime: 31 ms - beats 90.34%
Memory: 21.38 MB - beats 59.10%
"""
import tester


def solution(nums: list[int]) -> int:
    max_ones = 0
    curr = 0
    deleted = -1
    r = 0

    while r < len(nums):
        if nums[r]:
            # if a one, continue expanding window
            curr += 1
            if curr > max_ones:
                max_ones = curr
        elif deleted < 0:
            # if first zero, ignore and keep expanding
            deleted = r
        else:
            # if not first zero, move start of window to after previous delete
            curr = r - deleted - 1
            deleted = r
        r += 1

    return min(max_ones, len(nums)-1) # account for if all ones

tester.test([[1,1,0,1]], 3, solution)
tester.test([[0,1,1,1,0,1,1,0,1]], 5, solution)
tester.test([[1,1,1]], 2, solution)
