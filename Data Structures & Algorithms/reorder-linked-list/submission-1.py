# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        maybe a two pass solution?

        first pass stores all of the nodes we need to use,
        second pass sets them. O(n) space tho

        After hints:
        maybe one pass to figure out the length
        second to set two variables for the two halfs (and maybe reverse the second half) 
        
        third "pass" (not really) is to use the two variables to 
        flip flop back and forth and reorder somehow 

        [1, 2, 3, 4, 5]
        '''

        # first pass

        length = 0

        first = head

        while first:
            length += 1
            first = first.next
        print(f"length is {length}")
        # we have the length, now we make our pointers and reverse the second half

        l1 = head
        l2 = None # needs to be the end (which is the beginning of second half when reversed)

        pointer = head
        print(f"pointer is at {pointer.next}")
        counter = 0
        prev = None

        while pointer.next != None:
            

            if counter >= (length//2):
                # do reversing
                print(f"reversing {pointer.val}")
                temp = pointer.next
                pointer.next = prev
                prev = pointer
                pointer = temp
            else:
                counter += 1
                pointer = pointer.next
            print(counter)

        # pointer should be
        pointer.next = prev
        l2 = pointer

        # now we iterate through l1, do the thing
        ret = ListNode()
        pointer = ret

        for _ in range(length//2):
            pointer.next = l1
            pointer = pointer.next
            l1 = l1.next

            pointer.next = l2
            pointer = pointer.next
            l2 = l2.next

        return None




