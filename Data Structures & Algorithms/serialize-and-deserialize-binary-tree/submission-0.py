# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    '''
    what if we just tried to do neetcode way?

    serialize the tree using a string, none can be # or something
    how do we express different numbers correctly? like 892 or 213, probably another character
    for a seperator

    as for traversal method
    we could do bfs (how neetcode does it)
    '''

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        string = ""

        def dfs(root):
            nonlocal string

            if not root:
                string += "N#"
                return None 

            string += str(root.val) + "#"

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        print(string)
        return string


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        ls = data.split("#")
        counter = 0

        def dfs(root):
            nonlocal ls
            nonlocal counter
            if counter >= len(ls):
                return None

            rootString = ls[counter]

            if rootString == "N":
                counter += 1
                return None
            
            root = TreeNode(int(rootString))
            counter += 1

            root.left = dfs(root.left)
            root.right = dfs(root.right)

            return root
        
        return dfs(None)


