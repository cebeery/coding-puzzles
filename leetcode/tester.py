"""
Simple method to run examples for LeetCode problems
"""
def test(inputs: list, expected, method: callable):
    actual = method(*inputs)
    print(f'Expected: {expected} - Actual: {actual} - Passed? {expected == actual}')

def test_inplace(inputs: list, expected, method: callable, inplace_comparison_selector: callable):
    result = method(*inputs)
    if result is not None:
        actual = [result, inplace_comparison_selector(inputs, result)]
    else:
        actual = inplace_comparison_selector(inputs)
    print(f'Expected: {expected} - Actual: {actual} - Passed? {expected == actual}')


class ListNode:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.next: ListNode | None = nxt

    def __eq__(self, other):
        return (isinstance(other, ListNode) and
                self.val == other.val and
                self.next == other.next)

    def __str__(self):
        return f'{self.val}->{self.next}'

    @staticmethod
    def create(vals: list) -> 'ListNode':
        head = ListNode()
        curr = head
        for v in vals:
            nxt = ListNode(v)
            curr.next, curr = nxt, nxt
        return head.next

    @staticmethod
    def to_list(head: 'ListNode') -> list:
        nodes = [head]
        curr = head
        while e := curr.next:
            nodes.append(e.val)
            curr = e
        return nodes