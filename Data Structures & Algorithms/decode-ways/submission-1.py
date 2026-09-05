class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        we need to do dp, keep a list for each index,

        at every index, what do we need to know?

        well, at every index, if its 1 or 2, and we have a next number, then we know we have +2 ways of decoding the string, 
        either choosing that 1 or 2, OR using the next letter as the mapping, skipping that next letter

        similar to the house robber problem


        '''

        ret = 0
        n = len(s)
        memo = [-1] * n
        

        def dfs(i):

            if i >= n:
                return 1

            if memo[i] != -1:
                return memo[i]

            # if 0, nothing and skip the next one i+2
            if s[i] == "0":
                return 0

            memo[i] = (dfs(i+1))
            # if 1 or 2, get the sum? multiplication? of if you picked both or just one
            if (i + 1 < n) and (s[i] == "1" or (s[i] == "2" and s[i+1] < "7")):
                memo[i] += dfs(i+2)

            return memo[i]

        return dfs(0)
            



