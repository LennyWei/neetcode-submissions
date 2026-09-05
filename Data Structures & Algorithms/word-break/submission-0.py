class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        so at every decision, we need to choose between each word in wordDict

        example that means we need dp:
        s = "applepenappleacian", wordDict = ["apple","pen","appleacian"]


        at "applepen", we need to choose appleacian instead of apple.

        how can we memoize?

        well we can keep a dp hashmap that maps index:True/False whether theres a fitting word
        '''

        n = len(s)
        dp = {}


        def dfs(i):

            if i > n:
                return False
            elif i == n:
                return True
            
            if i in dp: # memoization 
                return dp[i]

            # choose between the choices
            found = False

            for word in wordDict:
                length = len(word)
                if s[i:i+length] == word:
                    # continue 
                    found = dfs(i+length)
                    if found:
                        break
            
            dp[i] = found

            return found

        return dfs(0)
                
