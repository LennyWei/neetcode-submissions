# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        retHead = ListNode() # dummy first node
        follower = retHead
        
        carryOne = False

        # wihle either pointer still exists
        while l1 or l2:
            
            l1Val = l1.val if l1 is not None else 0
            l2Val = l2.val if l2 is not None else 0

            total = l1Val + l2Val

            if carryOne:
                total += 1
                carryOne = False
            # carryone is false at this point

            if total >= 10:
                total = total % 10
                carryOne = True

            newNode = ListNode(total)
            follower.next = newNode
            follower = follower.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carryOne:
            follower.next = ListNode(1)

        return retHead.next

