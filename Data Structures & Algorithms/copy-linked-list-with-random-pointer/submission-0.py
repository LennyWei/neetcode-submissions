"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        To make a deep copy, we can easily make the original linked list (by iterating through)

        The problem is random.

        looking at topics, we could use a hashmap
        a listnode can be used as a key for a hashmap
        To make the copy, we prob need to use two passes, one to make the original linked list structure
        and the other to set the random pointers.

        way to hashmap: 
        map the original node to the corresponding new copy node
        '''

        hashmap = {None:None}

        follower = head
        while follower:
            # make the copy (no need to assign next or randoms right now)
            c = Node(follower.val) # could use a copyFollower val to set next here
            # no need to check is follower in hash, should always be unique
            hashmap[follower] = c
            follower = follower.next

        follower = head
        while follower:
            copyNow = hashmap[follower]
            copyNext = hashmap[follower.next]
            copyRandom = hashmap[follower.random]

            copyNow.next = copyNext
            copyNow.random = copyRandom

            follower = follower.next

        return hashmap[head]


            