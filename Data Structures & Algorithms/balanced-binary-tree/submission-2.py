# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        we return false only when there's a situation where it's left left, or right right 
        '''
        if not root:
            return True

        res = True

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            leftHeight = 0
            rightHeight = 0

            if root.left:
                leftHeight = dfs(root.left)
            if root.right:
                rightHeight = dfs(root.right)
            
            print(f"at root {root.val}, leftHeight = {leftHeight} and rightHeight = {rightHeight}")

            if abs(leftHeight - rightHeight) > 1:
                res = False
            
            return 1 + max(leftHeight, rightHeight)


        dfs(root)
        return res


