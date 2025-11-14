"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index
is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array,
then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.

Return the leftmost pivot index.
If no such index exists, return -1.

Constraints:
1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
-----------
Results
Runtime: 3 ms - beats 87.56%
Memory: 19.34 MB - beats 6.85%
"""
import tester

def solution(nums: list[int]) -> int:
    f_sum = [0]
    for num in nums:
        f_sum.append(f_sum[-1]+num)

    b_sum = [0]
    for num in reversed(nums):
        b_sum.append(b_sum[-1] + num)
    b_sum.pop()
    b_sum.reverse()

    for i in range(len(nums)):
        if f_sum[i] == b_sum[i]:
            return i
    return -1


tester.test([[1,7,3,6,5,6]], 3, solution)
tester.test([[1,2,3]], -1, solution)
tester.test([[2,1,-1]], 0, solution)
