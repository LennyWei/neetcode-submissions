class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.children = {}

class PrefixTree:

    def __init__(self):
        '''
        so essentially we keep a tree of nodes whose childrens are of val, node, pairs
        '''
        self.root = Node("#") # dummy first node
        self.wordList = {}

    def insert(self, word: str) -> None:
        follower = self.root
        self.wordList[word] = 67

        for char in word:

            if char not in follower.children:
                follower.children[char] = Node(char)
            # move to that node
            follower = follower.children[char]


    def search(self, word: str) -> bool:
        # how do we know that a current node we are on is the end of a word?

        if word not in self.wordList:
            return False
        else:
            return True
        

    def startsWith(self, prefix: str) -> bool:
        follower = self.root

        for char in prefix:
            # traverse through, return false if not where it should be
            if char not in follower.children:
                return False
            follower = follower.children[char]
        
        return True