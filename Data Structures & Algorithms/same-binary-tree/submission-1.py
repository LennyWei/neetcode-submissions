# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        so im thinking a dfs function that rnus two dfs parallel and compares the two vals
        '''
        res = True

        def dfs(root1, root2):
            nonlocal res

            if not root1 or not root2:
                if root1 != root2:
                    res = False
                return
            
            if root1.val != root2.val:
                res = False

            dfs(root1.left, root2.left)
            dfs(root1.right, root2.right)
        
        dfs(p, q)

        return res