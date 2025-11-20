"""
Given the head of a singly linked list,
group all the nodes with odd indices together
followed by the nodes with even indices,
and return the reordered list.

The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Constraints:
The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
-----------
Results
Runtime: 0 ms - beats 100.00%
Memory: 19.03 MB - beats 94.58%
"""
import tester
from tester import ListNode


def solution(head: ListNode|None) -> ListNode|None:
    if not head or not head.next:
        return head

    odd, even, even_head = head, head.next, head.next
    curr = even.next
    while curr:
        odd.next, odd = curr, curr
        even.next, even = curr.next, curr.next
        curr = None if not even else curr.next.next

    odd.next = even_head
    return head


tester.test([ListNode.create([1,2,3,4,5])], ListNode.create([1,3,5,2,4]), solution)
tester.test([ListNode.create([2,1,3,5,6,4,7])], ListNode.create([2,3,6,7,1,5,4]), solution)
