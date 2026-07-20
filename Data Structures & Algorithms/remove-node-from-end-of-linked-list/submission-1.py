# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        find the length, then length-n, thats the index to remove, second pass, boom
        '''

        # find the length
        length = 0

        follower = head
        while follower:
            length += 1
            follower = follower.next
        
        indexToRemove = length-n

        if indexToRemove == 0:
            return head.next
        
        prev = None
        follower = head
        counter = 0 

        while counter < indexToRemove:
            prev = follower
            follower = follower.next
            counter+=1

        print(counter)

        prev.next = follower.next

        return head