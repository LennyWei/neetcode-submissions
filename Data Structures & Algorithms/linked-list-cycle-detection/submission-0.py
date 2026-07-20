# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head

        counter = 0

        while fast:

            fast = fast.next

            counter += 1

            if fast is slow:
                return True

            if (counter % 2) == 0:
                slow = slow.next
        
        return False
