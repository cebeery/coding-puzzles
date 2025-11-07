"""
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's,
where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed
without violating the no-adjacent-flowers rule and false otherwise.

Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
-----------
Results
Runtime: 4 ms - beats 85.62%
Memory: 18.11 MB - beats 55.56%
"""
import tester


def solution(flowerbed: list[int], n: int) -> bool:
        empty_ct = 1
        plots = len(flowerbed)
        i = 0

        while n > 0 and i < plots:
            if flowerbed[i] == 0:
                empty_ct += 1
                if empty_ct > 2:
                    # plant flower in center of 3 empty plots, leaving rightmost plot still empty
                    empty_ct = 1
                    n -= 1
            else:
                # found a flower so no empty plots could be filled
                empty_ct = 0
            i += 1

        if empty_ct == 2:
            # if reached end of plots and last 2 were empty, plant in last plot
            n -= 1

        return n <= 0


tester.test([[1,0,0,0,1],1], True, solution)
tester.test([[1,0,0,0,1],2], False, solution)
