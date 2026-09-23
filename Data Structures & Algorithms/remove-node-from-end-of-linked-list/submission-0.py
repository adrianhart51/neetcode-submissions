# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [5, 4, 3, 2, 1, 0]
        #  s  e

        # use dummy node to handle empty and single node
        dummy = ListNode()
        dummy.next = head

        # move right pointer N times
        left = right = dummy
        move_count = 0
        while right and move_count < n:
            right = right.next
            move_count += 1
        
        # until right pointer reach the end, move both left and right pointer together
        # left pointer will be the removed node
        while left.next and right.next:
            left = left.next
            right = right.next

        # start previous next set to start next to remove the start node
        left.next = left.next.next

        return dummy.next
        