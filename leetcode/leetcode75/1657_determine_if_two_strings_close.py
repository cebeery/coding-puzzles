"""
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb

Operation 2: Transform every occurrence of one existing character into another existing character,
and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2,
return true if word1 and word2 are close, and false otherwise.

Constraints:
1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
-----------
Results
Runtime: 78 ms - beats 92.72%
Memory: 18.12 MB - beats 75.78%
"""
from collections import Counter

import tester


def solution(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        # Neither operation can change word length
        return False

    # Count letter frequency
    freq1 = Counter(word1)
    freq2 = Counter(word2)

    if freq1.keys() != freq2.keys():
        # Neither operation can add new letters
        return False

    # Count frequency of letter frequencies
    freq1 = Counter(freq1.values())
    freq2 = Counter(freq2.values())

    # Neither operation can change create a new letter frequency
    return freq1 == freq2



tester.test(['abc', 'bca'], True, solution)
tester.test(['a', 'aa'], False, solution)
tester.test(['cabbba', 'abbccc'], True, solution)
