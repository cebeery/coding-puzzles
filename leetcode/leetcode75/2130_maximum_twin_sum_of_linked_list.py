"""
In a linked list of size n, where n is even,
the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node,
if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2.
These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length,
return the maximum twin sum of the linked list.

Constraints:
The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105
-----------
Results
Runtime: 51 ms - beats 95.15%
Memory: 47.70 MB - beats 33.26%
"""
import tester
from tester import ListNode


def solution(head: ListNode) -> int:
    # Convert to list
    nodes = [head.val]
    curr = head
    while e := curr.next:
        nodes.append(e.val)
        curr = e

    # Pair ends
    max_twin = 0
    for i in range(len(nodes)//2):
        twin_sum = nodes[i] + nodes[-i-1]
        if max_twin < twin_sum:
            max_twin = twin_sum

    return max_twin


tester.test([ListNode.create([5,4,2,1])], 6, solution)
tester.test([ListNode.create([4,2,2,3])], 7, solution)
tester.test([ListNode.create([1,100000])], 100001, solution)
