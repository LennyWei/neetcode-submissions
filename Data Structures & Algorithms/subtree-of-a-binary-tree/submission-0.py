# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        time comp makes me think that we have to, at every potential subroot starter, try to explore, then reset
        if we didn't find it in that iteration

        '''
        res = False

        def dfs(root):
            nonlocal subRoot
            
            if not root:
                return False
            
            if root.val == subRoot.val:
                found = sameTree(root, subRoot)

                if found:
                    return True
            
            return dfs(root.left) or dfs(root.right)
            

        
        def sameTree(root1, root2):
            # Same Binary Tree Implementation
            if not root1 or not root2:
                if root1 != root2:
                    return False
                return True
            
            if root1.val != root2.val:
                return False
            
            return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)
        
        return dfs(root)
            