# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        node1
        self.val = 0
        self.next = node2

        node2
        self.val = 1
        self.next = None
        '''

        if not head:
            return None

        prevNode = None
        currentNode = head
        nextNode = head.next
        
        
        currentNode.next = None
        

        while nextNode: # while the next is still good
            
            prevNode = currentNode # node1
            currentNode = nextNode # node2
            nextNode = nextNode.next # None

            currentNode.next = prevNode

        return currentNode