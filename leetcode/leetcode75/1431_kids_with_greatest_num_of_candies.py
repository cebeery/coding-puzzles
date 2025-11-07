"""
There are n kids with candies.
You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has,
and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n,
where result[i] is true if, after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

Constraints:
n == candies.length
2 <= n <= 100
1 <= candies[i] <= 100
1 <= extraCandies <= 50
-----------
Results
Runtime: 0 ms - beats 100.00%
Memory: 17.84 MB - beats 34.07%
"""
import tester


def solution(candies: list[int], extraCandies: int) -> list[bool]:
    max_raw = max(candies) - extraCandies
    output = [False] * len(candies)
    for i, kid in enumerate(candies):
        if kid >= max_raw:
            output[i] = True

    return output


tester.test([[2,3,5,1,3],3], [True,True,True,False,True], solution)
tester.test([[4,2,1,1,2],1], [True,False,False,False,False], solution)
tester.test([[12,1,12],10], [True,False,True], solution)
