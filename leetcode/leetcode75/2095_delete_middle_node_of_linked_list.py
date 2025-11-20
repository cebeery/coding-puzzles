"""
You are given the head of a linked list.
Delete the middle node,
and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing,
where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Constraints:
The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105
-----------
Results
Runtime: 36 ms - beats 98.44%
Memory: 48.94 MB - beats 51.59%
"""
from typing import Optional

import tester
from tester import ListNode

def solution(head: ListNode|None) -> ListNode|None:
    if not head or not head.next:
        return None

    prev, slow, fast = None, head, head.next
    while fast:
        prev = slow
        slow = slow.next # Move once
        if fast.next: # Move twice
            fast = fast.next.next
        else:
            fast = None

    prev.next = slow.next
    return head


tester.test([ListNode.create([1,3,4,7,1,2,6])], ListNode.create([1,3,4,1,2,6]), solution)
tester.test([ListNode.create([1,2,3,4])], ListNode.create([1,2,4]), solution)
tester.test([ListNode.create([2,1])], ListNode.create([2]), solution)

