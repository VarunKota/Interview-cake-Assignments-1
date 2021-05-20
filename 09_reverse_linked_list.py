""" Write a function for reversing a linked list.
Your function will have one input: the head of the list.
Your function should return the new head of the list.

Here's a sample linked list node class:

  class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None   """

# Start coding from here
class ListNode:
    def _init_(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        head, next = self._recursive(head)
        _next.next = None
        return head

    def __recursive(self, head: ListNode) -> (ListNode, ListNode):
        if not head.next:
            return head, head

        node, next = self._recursive(head.next)
        _next.next = head

        return node, head


if _name_ == "_main_":
    solution = Solution()

    head = ListNode(1, ListNode(2))
    head.next = ListNode(3)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(5)

    print(solution.reverseList(head))
