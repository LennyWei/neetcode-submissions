# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        dfs, keep return true unless we break the rules
        '''

        def dfs(root, interval):

            if not root:
                return True
        

            if root.left and (root.left.val >= root.val or root.left.val <= interval[0]):
                return False


            if root.right and (root.right.val <= root.val or root.right.val >= interval[1]):
                return False
        

            
            

            return dfs(root.left, [interval[0], root.val]) and dfs(root.right, [root.val, interval[1]])
        
        return dfs(root, [-math.inf, math.inf])