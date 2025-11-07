"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string
by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining characters.
 (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
-----------
Results
Runtime: XX ms - beats XX.XX%
Memory: XX MB - beats XX.XX%
"""
import tester


def solution(s: str, t: str) -> bool:
        desired = 0
        search = 0

        while desired < len(s) and search < len(t):
            if s[desired] == t[search]:
                desired += 1
            search += 1

        return desired >= len(s)


tester.test(['abc','ahbgdc'], True, solution)
tester.test(['axc','ahbgdc'], False, solution)
