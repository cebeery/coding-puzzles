"""
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string],
 where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid;
there are no extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k.
For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Constraints:
1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
-----------
Results
Runtime: 0 ms - beats 100.00%
Memory: 17.78 MB - beats 54.14%
"""
import tester


def solution(s: str) -> str:
    def stringify(l):
        return ''.join(l)

    stack = []
    word = []
    integer = []
    for c in s:
        if c != ']':
            stack.append(c)
        else:
            # Construct sequence to repeat
            while stack[-1] != '[':
                word.append(stack.pop())

            stack.pop() # Discard bracket

            # Construct num of reps
            while stack and stack[-1].isdigit():
                integer.append(stack.pop())

            # Repeat section and add to stack
            reps = int(stringify(reversed(integer)))
            section = list(reversed(word))*reps
            stack.append(stringify(section))

            # Reset trackers
            word = []
            integer = []
    return stringify(stack)

tester.test(['3[a]2[bc]'], 'aaabcbc', solution)
tester.test(['3[a2[c]]'], 'accaccacc', solution)
tester.test(['2[abc]3[cd]ef'], 'abcabccdcdcdef', solution)
