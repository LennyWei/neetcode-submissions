# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        dfs, as we visit nodes (starting from the bottom) add to a global counter?
        would that gaurentee we explore nodes from smallest to largest?


        '''
        counter = 0
        ret = -1

        def dfs(root):
            nonlocal counter
            nonlocal k
            nonlocal ret

            x = None
            if not root:
                return None

            
            if root.left:
                dfs(root.left)
            
            counter += 1
            print(f"added at {root.val}, counter is now {counter}")

            if counter == k:
                ret = root.val

            
            if root.right:
                dfs(root.right)
            

            return None
        
        dfs(root)

        return ret