class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = [-1] * n


        def dfs(i):
            if i == n: # we reach the last step, add a valid one
                return 1
            elif i > n: # we go over, no good
                return 0
            
            if cache[i] != -1: # if it's cached, we return it
                return cache[i]

            cache[i] = dfs(i+1) + dfs(i+2)

            return cache[i]
        
        return dfs(0)
