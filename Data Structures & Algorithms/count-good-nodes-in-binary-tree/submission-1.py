# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        im thinkin normal dfs, and we keep like a "maxSoFar" variable that we pass down 
        '''
        ret = 0

        def dfs(root, maxSoFar):
            nonlocal ret

            if not root:
                return None

            if root.val >= maxSoFar:
                ret += 1
                maxSoFar = root.val
            
            dfs(root.left, maxSoFar)
            dfs(root.right, maxSoFar)

        dfs(root, -101)

        return ret
