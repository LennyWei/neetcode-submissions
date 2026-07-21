# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        is this not just bfs
        '''

        ret = []
        queue = []

        if root:
            queue.append(root)

        while queue: 

            sublist = []
            # loop through
            queueLength = len(queue)

            for _ in range(queueLength): # only looks at the original stuff, not the newly added nodes

                node = queue.pop(0)
                sublist.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            print(f"sublist is {sublist}, queue is {queue}")
            ret.append(sublist)
        
        return ret
