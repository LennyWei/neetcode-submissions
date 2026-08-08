class Node:

    def __init__(self) -> None:
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        '''
        the dots mean that we need to recurse over all potential letters of that node, so that we dont miss any possibilities
        '''
        self.root = Node()


    def addWord(self, word: str) -> None:
        follower = self.root

        for char in word:

            if char not in follower.children:
                follower.children[char] = Node()
            
            follower = follower.children[char]
        
        follower.isEnd = True


    def search(self, word: str) -> bool:

        # need a helper function
        def dfs(currentNode, index):

            if index == len(word):
                if currentNode.isEnd:
                    return True
                else:
                    return False
            
            valid = False
            letter = word[index]

            if letter == ".":
                # look through all paths to find a valid path
                for key, value in currentNode.children.items():
                    valid = valid or dfs(value, index+1)

                    if valid:
                        break
                
                return valid
            elif letter in currentNode.children:
                # is good, continue
                return dfs(currentNode.children[letter], index+1)
            else:
                # not good, False
                return False




        return dfs(self.root, 0)

        
