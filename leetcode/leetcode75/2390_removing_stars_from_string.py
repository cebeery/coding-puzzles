"""
You are given a string s, which contains stars *.

In one operation, you can:
Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:
The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters and stars *.
The operation above can be performed on s.
-----------
Results
Runtime: 91 ms - beats 81.38%
Memory: 19.13 MB - beats 37.71%
"""
import tester


def solution(s: str) -> str:
    # Stack
    stack = []
    for l in s:
        if l == '*':
            stack.pop()
        else:
            stack.append(l)
    return ''.join(stack)

    # # Reversed Array (104 ms - beats 40.42%)
    # rm = 0
    # res = []
    # for l in reversed(s):
    #     if l == '*':
    #         rm += 1
    #     elif rm > 0:
    #         rm -= 1
    #     else:
    #          res.append(l)
    # return ''.join(reversed(res))


tester.test(['leet**cod*e'], 'lecoe', solution)
tester.test(['erase*****'], '', solution)
