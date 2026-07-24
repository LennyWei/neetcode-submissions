# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        iterate through preorder (get the root)

        '''
        hashmap = {}

        for index, val in enumerate(inorder):
            hashmap[val] = index
        print(hashmap)

        preOrderIndex = 0

        left = 0
        right = len(inorder) - 1

        def dfs(l, r):
            nonlocal preOrderIndex
            nonlocal hashmap


            if l > r:
                return None
            
            val = preorder[preOrderIndex]
            preOrderIndex += 1

            root = TreeNode(val)

            mid = hashmap[val]

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            
            return root

        return dfs(left, right)

