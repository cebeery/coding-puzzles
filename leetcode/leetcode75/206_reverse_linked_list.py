"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
-----------
Results
Runtime: 0 ms - beats 100.00%
Memory: 18.66 MB - beats 52.58%
"""
import tester
from tester import ListNode


def solution(head: ListNode|None) -> ListNode|None:
    prev, curr = None, head
    while curr:
        nxt, curr.next = curr.next, prev
        prev, curr = curr, nxt

    return prev

tester.test([ListNode.create([1,2,3,4,5])], ListNode.create([5,4,3,2,1]), solution)
tester.test([ListNode.create([1,2])], ListNode.create([2,1]), solution)
tester.test([ListNode.create([])], ListNode.create([]), solution)
