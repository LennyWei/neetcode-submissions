# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        Binary search tree properties: sorted from left to right, meaning at every node, the left is smaller, 
        and right is bigger

        so given the root node: 5, and 3 and 8

        we want to have a root that is right between 3 and 8
        in other words, the node we're looking at has to be root >= 3, and <= 8 

        if it was like 1, 4, then we know to look left
        '''

        # wanna make sure that p is always the lower one
        if q.val < p.val:
            temp = p
            p = q
            q = temp
        print(f"p is {p.val} and q is {q.val}")
        ret = None

        def dfs(root):
            nonlocal ret
            if root is None:
                return "error"
            print(f"searching {root.val}")
            
            # the rule we came up with
            if root.val >= p.val and root.val <= q.val:
                ret = root
                print(f"setting ret")
            elif root.val >= p.val and root.val >= q.val: # if root is bigger than both
                dfs(root.left)
            elif root.val <= p.val and root.val <= q.val: # if root is smaller than both
                dfs(root.right)
        
        dfs(root)

        return ret



            