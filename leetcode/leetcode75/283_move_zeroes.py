"""
Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
-----------
Results
Runtime: 4 ms - beats 60.70%
Memory: 19.02 MB - beats 9.68%
"""
import tester


def solution(nums: list[int]) -> None:
        insert = 0
        for num in nums:
            if num != 0:
                nums[insert] = num
                insert += 1

        for i in range(insert, len(nums)):
            nums[i] = 0

def inplace_selector(inputs: list[list[int]], result: None) -> list[int]:
    return inputs[0]

tester.test_inplace([[0,1,0,3,12]], [None,[1,3,12,0,0]], solution, inplace_selector)
tester.test_inplace([[0]], [None,[0]], solution, inplace_selector)
