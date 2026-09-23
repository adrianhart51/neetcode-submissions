# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [5, 4, 3, 2, 1]
        #        l     r

        # use dummy node to handle empty and single node
        dummy = ListNode()
        dummy.next = head

        # move right pointer N times
        left = right = dummy
        for _ in range(n):
            right = right.next
        
        # until right pointer reach the end, move both left and right pointer together
        while right.next:
            left = left.next
            right = right.next

        # left pointer next will be the removed node
        left.next = left.next.next

        return dummy.next
        