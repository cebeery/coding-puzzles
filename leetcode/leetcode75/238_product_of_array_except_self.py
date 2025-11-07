"""
Given an integer array nums, return an array answer
such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
-----------
Results
Runtime: 19 ms - beats 87.11%
Memory: 26.10 MB - beats 30.41%
"""
import tester


def solution(nums: list[int]) -> list[int]:
        # Create array of the product of all previous values
        forward = [1]
        for num in nums:
            forward.append(forward[-1] * num)
        forward.pop()

        # Create array of the product of all upcoming values
        reverse = [1]
        for num in reversed(nums):
            reverse.append(reverse[-1] * num)
        reverse.pop()
        reverse.reverse()
        # Tried doing ranges instead of 2x reverse and pop but was significantly less efficient when submitted

        # Construct self-exclusive product
        exclusive_products = [0]*len(nums)
        for i in range(len(nums)):
            exclusive_products[i] = forward[i] * reverse[i]

        return exclusive_products

tester.test([[1,2,3,4]], [24,12,8,6], solution)
tester.test([[-1,1,0,-3,3]], [0,0,9,0,0], solution)
