# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            m = self.search(root, 1)
        else:
            return 0
        return m

    
    def search(self, node, length):
        m = length

        if node.left:
            m = max(self.search(node.left, length+1), m)
        if node.right:
            m = max(self.search(node.right, length+1), m)
        
        return m