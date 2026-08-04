# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.next is None and l2.next is None:
            if l1.val + l2.val < 10:
                return ListNode(l1.val + l2.val)
            else:
                return ListNode((l1.val + l2.val) % 10, ListNode(1))
        elif l1.next is None:
            if l1.val + l2.val < 10:
                return ListNode(l1.val + l2.val, l2.next)
            else:
                return ListNode(
                    (l1.val + l2.val) % 10,
                    self.addTwoNumbers(ListNode(1), l2.next)
                )
        elif l2.next is None:
            if l1.val + l2.val < 10:
                return ListNode(l1.val + l2.val, l1.next)
            else:
                return ListNode(
                    (l1.val + l2.val) % 10,
                    self.addTwoNumbers(ListNode(1), l1.next)
                )
        else:
            remaining_part = self.addTwoNumbers(l1.next, l2.next)
            return ListNode(
                (l1.val + l2.val) % 10,
                self.addTwoNumbers(ListNode((l1.val + l2.val) // 10), remaining_part)
            )
