# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0, 1, 2, 3, 4, 5, 6]
        
        # find half
        # [0, 1, 2, 3]
        # [4, 5, 6]
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse last half of the node
        # [0, 1, 2, 3]
        # [6, 5, 4]
        prev, curr = None, slow
        while curr:
            next_ = curr.next
            curr.next = prev
            prev, curr = curr, next_

        # merge first half and second half
        # []
        # []
        # [0, 6, 1, 5, 2, 4, 3]
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next