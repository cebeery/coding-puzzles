"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words.
Do not include any extra spaces.

Constraints:
1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
-----------
Results
Runtime: 0 ms - beats 100.00%
Memory: 18.01 MB - beats 23.58%
"""
import tester


def solution(s: str) -> str:
        words = s.split()
        words.reverse()
        return ' '.join(words)


tester.test(['the sky is blue'], 'blue is sky the', solution)
tester.test(['  hello world  '], 'world hello', solution)
tester.test(['a good   example'], 'example good a', solution)
