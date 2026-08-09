class Node:

    def __init__(self, index = -1) -> None:
        self.children = {}
        self.isEnd = False
        self.index = index

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        similar problem to Backtracking: Word Search

        but instead here, we have multiple words, and we can have back, and backend, which uses "back" from back.

        '''
        root = Node()
        # first we add all words to trie

        for index, word in enumerate(words):
            follower = root
            for char in word:
                if char not in follower.children:
                    follower.children[char] = Node()
                follower = follower.children[char]
            follower.isEnd = True
            follower.index = index




        ROWS, COLS = len(board), len(board[0])
        path = set()
        follower = root
        ret = []

        def dfs(r, c):
            nonlocal follower
            nonlocal ret

            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or

                board[r][c] not in follower.children 
                
                or
                (r, c) in path):
                return False


            temp = follower
            follower = follower.children[board[r][c]]

            if follower.isEnd:
                if follower.index != -1:
                    ret.append(words[follower.index])
                    follower.index = -1

            

            path.add((r, c))
            res = (dfs(r + 1, c) or
                   dfs(r - 1, c) or
                   dfs(r, c + 1) or
                   dfs(r, c - 1))
            path.remove((r, c))
            follower = temp
            return res

        for r in range(ROWS):
            for c in range(COLS):
                follower = root
                dfs(r, c)

        return ret