"""
You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.

Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
-----------
Results
Runtime: 39 ms - beats 48.13%
Memory: 17.68 MB - beats 73.43%
"""
import tester
#import itertools

def solution(word1: str, word2: str) -> str:
    # Issue: Discards leftovers
    # return ''.join(i+j for i,j in zip(word1, word2))

    # Issue: itertools frowned on for interviews
    # return ''.join(i+j for i,j in itertools.zip_longest(word1, word2, fillvalue=''))

    # Issue: extraneous next calls if lists very different lengths
    iter1 = iter(word1)
    iter2 = iter(word2)
    zipped = ''

    while (append := next(iter1, '') + next(iter2, '') ) != '':
        zipped += append
    return zipped

tester.test(['abc', 'pqr'],'apbqcr', solution)
tester.test(['ab', 'pqrs'],'apbqrs', solution)
tester.test(['abcd', 'pq'],'apbqcd', solution)
