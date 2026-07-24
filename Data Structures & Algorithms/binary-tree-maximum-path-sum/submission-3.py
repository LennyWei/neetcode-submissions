# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        very similar to the diameter easy problem, at every node, we need to compute:

        a max of left + right path

        and one max path to return back

        '''
        maxPath = -math.inf


        def dfs(root):
            nonlocal maxPath

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            biggestPathHere = left + right + root.val

            print(f"we looking at {root.val}, {biggestPathHere}")
            maxPath = max(maxPath, biggestPathHere)
            
            return max(max(left, right) + root.val, 0) # use this path, or nah
        
        dfs(root)
        return maxPath

