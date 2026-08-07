class Node:
    def __init__(self, val, isEnd = False) -> None:
        self.val = val
        self.isEnd = isEnd
        self.children = {}

class PrefixTree:

    def __init__(self):
        '''
        so essentially we keep a tree of nodes whose childrens are of val, node, pairs
        '''
        self.root = Node("#") # dummy first node

    def insert(self, word: str) -> None:
        follower = self.root

        for char in word:
            if char not in follower.children:
                follower.children[char] = Node(char)
            # move to that node
            follower = follower.children[char]

        follower.isEnd = True

    def search(self, word: str) -> bool:
        # how do we know that a current node we are on is the end of a word? with a flag
        follower = self.root

        for char in word:
            # traverse through, return false if not where it should be
            if char not in follower.children:
                return False
            follower = follower.children[char]
        
        if follower.isEnd:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        follower = self.root

        for char in prefix:
            # traverse through, return false if not where it should be
            if char not in follower.children:
                return False
            follower = follower.children[char]
        
        return True