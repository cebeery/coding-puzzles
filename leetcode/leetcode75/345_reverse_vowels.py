"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u',
and they can appear in both lower and upper cases, more than once.

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
-----------
Results
Runtime: 7 ms - beats 89.97%
Memory: 18.69 MB - beats 48.23%
"""
import tester


def solution(s: str) -> str:
        vowels = set('AEIOUaeiou')
        l,r = 0, len(s)-1
        new_str = list(s)

        while l <= r:
            l_vowel, r_vowel = s[l] in vowels, s[r] in vowels
            if l_vowel and r_vowel: # if both are vowels, swap then move both pointers inward
                new_str[l] = s[r]
                new_str[r] = s[l]
                l += 1
                r -= 1
            elif l_vowel: # if only left is vowel, move right pointer
                r -= 1
            elif r_vowel: # if only right is vowel, move left pointer
                l += 1
            else: # both are not vowels
                l += 1
                r -= 1

        return ''.join(new_str)


tester.test(['IceCreAm'], 'AceCreIm', solution)
tester.test(['leetcode'], 'leotcede', solution)
