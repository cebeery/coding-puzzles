"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k)
such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.

Constraints:
1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
-----------
Results
Runtime: 11 ms - beats 96.61%
Memory: 37.62 MB - beats 23.59%
"""
import tester


def solution(nums: list[int]) -> bool:
    if len(nums) < 3:
        return False

    minimum = float('inf')
    second = float('inf')
    for num in nums:
        if num <= minimum:
            minimum = num
            # Note that this can cause the index of minimum to be higher than that of second
            # but if second is set then there must once have been an earlier index that was less than it
        elif num <= second:
            second = num
        else:
            # If second set and this is larger, than a triplet must exist
            return True
    return False


tester.test([[1,2,3,4,5]], True, solution)
tester.test([[5,4,3,2,1]], False, solution)
tester.test([[2,1,5,0,4,6]], True, solution)
tester.test([[0,4,2,1,0,-1,-3]], False, solution)