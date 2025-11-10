"""
Given a string s and an integer k,
return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
-----------
Results
Runtime: 47 ms - beats 95.01%
Memory: 18.02 MB - beats 56.61%
"""
import tester


def solution(s: str, k: int) -> int:
    vowels = {'a','e','i','o','u'}
    ct = 0

    # Construct initial
    for char in s[:k]:
        if char in vowels:
            ct += 1
    max_ct = ct

    # Slide window
    for i in range(k, len(s)):
        if ct == k:
            # Shortcut
            return ct


        if s[i] in vowels:
            ct += 1

        if s[i-k] in vowels:
            ct -= 1

        if ct > max_ct:
            max_ct = ct

    return max_ct


tester.test(['abciiidef', 3], 3, solution)
tester.test(['aeiou', 2], 2, solution)
tester.test(['leetcode', 3], 2, solution)
