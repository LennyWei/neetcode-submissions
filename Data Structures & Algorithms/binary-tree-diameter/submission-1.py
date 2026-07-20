# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        longest path

        at every node, we keep track of a "currentLine var that increases 
        '''
        
        return max(self.recurse(root))  
    
    def recurse(self, root):
        if root == None:
            return 0
        
        maxLeg = 0
        maxKnown = 0

        leftLeg = (0, 0)
        rightLeg = (0, 0)

        if root.left:
            leftLeg = self.recurse(root.left) # leftLeg is a tuple(maxLeg, maxKnown)
            leftLeg[0] += 1
        if root.right:
            rightLeg = self.recurse(root.right)
            rightLeg[0] += 1
        
        maxKnown = max(max(leftLeg[1], rightLeg[1]), leftLeg[0] + rightLeg[0])
    
        return [max(leftLeg[0], rightLeg[0]), maxKnown]
        