"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

Constraints:
1 <= nums1.length, nums2.length <= 1000
-1000 <= nums1[i], nums2[i] <= 1000
-----------
Results
Runtime: 3 ms - beats 94.12%
Memory: 17.96 MB - beats 90.33%
"""
import tester


def solution(nums1: list[int], nums2: list[int]) -> list[set[int]]:
    a = set(nums1)
    b = set(nums2)
    return [a-b,b-a]
    # return [list(a-b),list(b-a)]


tester.test([[1,2,3], [2,4,6]], [{1,3},{4,6}], solution)
tester.test([[1,2,3,3], [1,1,2,2]], [{3}, set()], solution)
