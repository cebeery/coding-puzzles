"""
Given an array of integers arr,
return true if the number of occurrences of each value in the array is unique
or false otherwise.

Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
-----------
Results
Runtime: 0 ms - beats 100.00%
Memory: 17.93 MB - beats 39.80%
"""
from collections import Counter

import tester


def solution(arr: list[int]) -> bool:
    freq = Counter(arr)
    return len(freq) == len(set(freq.values()))


tester.test([[1,2,2,1,1,3]], True, solution)
tester.test([[1,2]], False, solution)
tester.test([[-3,0,1,-3,1,1,1,-3,10,0]], True, solution)
