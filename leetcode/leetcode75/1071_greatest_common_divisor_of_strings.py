"""
For two strings s and t,
we say "t divides s" if and only if s = t + t + t + ... + t + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
-----------
Results
Runtime: 0 ms - beats 100.00%
Memory: 17.86 MB - beats 46.54%
"""
import tester

def solution(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        # If no gcd
        return ''

    len1 = len(str1)
    len2 = len(str2)
    prefix = str2 if len1 > len2 else str1
    lenp = len(prefix)

    while lenp > 1:
        if len1 % lenp == 0 and len2 % lenp == 0 :
            # if length of candidate a common divisor of both inputs
            # and gcd existence already established
            return prefix
        prefix = prefix[:-1]
        lenp -= 1

    return prefix


tester.test(['ABCABC', 'ABC'],'ABC', solution)
tester.test(['ABABAB', 'ABAB'],'AB', solution)
tester.test(['LEET', 'CODE'],'', solution)
