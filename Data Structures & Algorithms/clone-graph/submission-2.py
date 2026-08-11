"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        keep a dictionary mapping val to node (the NEW node),

        given the node, if doesn't exist, make a new one and add it to the hashmap.
        
        iterate through the neighbor list, creating them if they not in hash, then adding them to the current new node's neighbors
        '''
        if not node:
            return None

        hashmap = {}
        firstNode = None

        def recurse(n, first = False):
            nonlocal hashmap
            nonlocal firstNode

            if n.val not in hashmap:
                newNode = Node(n.val)
                hashmap[n.val] = newNode
            
            if first:
                firstNode = hashmap[n.val]

            for neighbor in n.neighbors:

                if neighbor.val not in hashmap:
                    newNeighbor = Node(neighbor.val)
                    hashmap[neighbor.val] = newNeighbor
                    recurse(neighbor)
                
                # the new current node, add all of the neighbors
                hashmap[n.val].neighbors.append(hashmap[neighbor.val])
            
        

        recurse(node, True)

        return firstNode
            
