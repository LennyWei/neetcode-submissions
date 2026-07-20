# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        so at every parent node, we need to flip the child nodes.
        '''
        if not root:
            return None

        def recurse(node):
            print(f"recursing {node.val}")

            if node.left == None and node.right == None:
                print(f"leaf node")
                return node
            elif node.left == None:
                node.left = recurse(node.right)
                node.right = None
                return node
            elif node.right == None:
                node.right = recurse(node.left)
                node.left = None
                return node
            
            temp = node.left
            node.left = recurse(node.right)
            node.right = recurse(temp)
            return node
        
        return recurse(root)
