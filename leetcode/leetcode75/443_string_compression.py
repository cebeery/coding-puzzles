"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Note: The characters in the array beyond the returned length do not matter and should be ignored.

Constraints:
1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
-----------
Results
Runtime: 0 ms - beats 100.00%
Memory: 17.77 MB - beats 94.44%
"""
import tester


def solution(chars: list[str]) -> int:
        output_idx = 0
        group = ''
        cnt = 0

        def add_group_count():
            if cnt > 1:
                nonlocal output_idx
                nonlocal chars
                cnt_str = str(cnt)
                for c in cnt_str:
                    # 15 -> '1','5'
                    chars[output_idx] = c
                    output_idx += 1

        for char in chars.copy():
            if char != group:
                add_group_count()
                chars[output_idx] = char
                output_idx += 1
                group = char
                cnt = 1
            else:
                cnt += 1
        add_group_count()

        return output_idx

def inplace_selector(inputs: list[list[int]], result: int) -> list[int]:
    return inputs[0][0:result]

tester.test_inplace([["a","a","b","b","c","c","c"]], [6,["a","2","b","2","c","3"]], solution, inplace_selector)
tester.test_inplace([["a"]], [1,["a"]], solution, inplace_selector)
tester.test_inplace([["a","b","b","b","b","b","b","b","b","b","b","b","b"]], [4,["a","b","1","2"]], solution,
                    inplace_selector)
