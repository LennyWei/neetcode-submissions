# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        while loop, compare the two current values, keep temp variables

        '''
        head = ListNode() # dummy node
        print("Hello")

        ls1 = list1
        ls2 = list2
        follower = head
        
        while ls1 and ls2:
            
            print(f"ls1 is {ls1.val} and ls2 is {ls2.val}")
            if ls1.val >= ls2.val:
                follower.next = ls2
                ls2 = ls2.next
            else:
                follower.next = ls1
                ls1 = ls1.next
            
            follower = follower.next

        if ls1:
            follower.next = ls1
        elif ls2:
            follower.next = ls2

        return head.next