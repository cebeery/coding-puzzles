"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value
and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Constraints:
n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
-----------
Results
Runtime: 48 ms - beats 89.96%
Memory: 27.31 MB - beats 75.66%
"""
import tester


def solution(nums: list[int], k: int) -> float:
    # Construct initial guess
    l, r = 0, k
    max_sum = curr_sum = sum(nums[:k])

    # Slide window
    while r < len(nums):
        curr_sum += nums[r] - nums[l]
        if max_sum < curr_sum:
            max_sum = curr_sum

        r += 1
        l += 1

    return max_sum / k


tester.test([[1,12,-5,-6,50,3], 4], 12.75, solution)
tester.test([[5], 1], 5.0, solution)
