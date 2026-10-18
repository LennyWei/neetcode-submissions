# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
reversing a linked list involves keeping a temp variable of the prev as you iterate through the linked list.
'''



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        pointer = head
        prev = None

        while pointer.next != None:
            # ordering matters, 
            temp = pointer.next
            pointer.next = prev
            prev = pointer

            pointer = temp
        
        pointer.next = prev

        return pointer

            