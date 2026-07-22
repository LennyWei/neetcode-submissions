# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ret = []
        queue = []

        if root:
            queue.append(root)

        while queue: 
            ret.append(queue[-1].val)

            # loop through
            queueLength = len(queue)

            for _ in range(queueLength): # only looks at the original stuff, not the newly added nodes

                node = queue.pop(0)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            print(f"queue is {queue}")
            
        
        return ret