class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        at every recursion, we decide whether to open or close a parenthesis
        we pass through a "open so far" vairable, when it gets to n, we close until currentClosings
        gets to n, when they both n, we return

        '''

        ret = []
        def dfs(string, currentOpenings, currentClosings):
            nonlocal ret

            if currentOpenings == n:
                if currentClosings == n:
                    ret.append(string)
                else:
                    dfs(string + ")", currentOpenings, currentClosings + 1)
                return 
            
            # open
            dfs(string + "(", currentOpenings + 1, currentClosings)

            # close
            if currentOpenings != currentClosings:
                dfs(string + ")", currentOpenings, currentClosings + 1)
        
        dfs("", 0, 0)
        return ret


